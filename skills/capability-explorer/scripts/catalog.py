#!/usr/bin/env python3
"""Bounded local recall and URL-keyed upserts. Storage transfers belong to the host."""
import argparse
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

def canonical(url):
    p = urlsplit(url)
    if p.scheme not in ("http", "https") or not p.hostname or p.username or p.password:
        raise ValueError("Expected a public repository/tool URL without credentials")
    path = p.path.rstrip("/")
    if p.hostname.lower() == "github.com":
        parts = path.strip("/").split("/")
        if len(parts) < 2:
            raise ValueError("Expected owner/repository")
        path = "/" + "/".join(parts[:2]).removesuffix(".git").lower()
    return "https://" + p.netloc.lower() + path

def load(path):
    data = json.loads(Path(path).read_text())
    if data.get("schema_version") != 1 or not isinstance(data.get("entries"), list):
        raise ValueError("Unsupported catalog schema")
    seen = set()
    for row in data["entries"]:
        key = canonical(row["url"])
        if key in seen:
            raise ValueError("Duplicate repository URL")
        seen.add(key)
    return data

def query(data, words, limit=5, expanded=False):
    cap, budget = (15, 30000) if expanded else (5, 12000)
    if not 1 <= limit <= cap:
        raise ValueError("Limit exceeds selected exploration scope")
    terms = set(re.findall(r"[a-z0-9]+", words.lower()))
    matches = []
    for row in data["entries"]:
        searchable = json.dumps({k: row.get(k) for k in
            ("name", "url", "tags", "capabilities", "interfaces", "project_relevance", "inferred_ideas")}).lower()
        tokens = set(re.findall(r"[a-z0-9]+", searchable))
        score = len(terms & tokens)
        if score:
            matches.append((score, row))
    matches.sort(key=lambda item: (-item[0], item[1]["url"]))
    selected, used = [], 0
    for score, row in matches[:limit]:
        size = len(json.dumps(row, ensure_ascii=False))
        if used + size > budget:
            break
        selected.append({"score": score, "record": row})
        used += size
    return {"catalog_entries": len(data["entries"]), "matching_entries": len(matches),
            "returned_entries": len(selected), "record_characters": used,
            "scope": "expanded" if expanded else "standard",
            "more_available": len(matches) > len(selected),
            "offer_broader_pass": len(matches) > len(selected) or len(data["entries"]) > 100,
            "records": selected}

def upsert(data, record):
    key = canonical(record["url"])
    record = dict(record, url=key)
    for i, existing in enumerate(data["entries"]):
        if canonical(existing["url"]) == key:
            data["entries"][i] = dict(existing, **record)
            break
    else:
        data["entries"].append(record)
    data["updated_at"] = datetime.now(timezone.utc).isoformat()
    return data

def save(path, data):
    path = Path(path)
    fd, temporary = tempfile.mkstemp(dir=path.parent, prefix=".catalog-")
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump(data, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["query", "upsert", "validate"])
    parser.add_argument("path")
    parser.add_argument("--query", default="")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--expanded", action="store_true")
    parser.add_argument("--record")
    args = parser.parse_args()
    data = load(args.path)
    if args.action == "query":
        result = query(data, args.query, args.limit, args.expanded)
    elif args.action == "upsert":
        if not args.record:
            parser.error("upsert requires --record")
        save(args.path, upsert(data, json.loads(Path(args.record).read_text())))
        result = {"saved_locally": True, "durable_writeback_required": True}
    else:
        result = {"valid": True, "entries": len(data["entries"])}
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
