# Cross-chat catalog

Use this reference when an exploration catalog is available or the user requests persistent recall.

## Storage and authorization

The portable public skill contains this protocol and local helper, never the user's history.
In ChatGPT Work, use the Library skill to resolve the exact filename
`Capability_Explorer_Catalog.json`; elsewhere use a user-designated durable store.
Never assume local scratch storage survives chats. If storage is unavailable, continue
without memory and disclose that no update was saved.

The catalog's `settings.auto_save_explorations` records explicit user opt-in.
Honor that setting and current instructions. Do not create or enable a catalog without
authorization. Opt-in permits saving a compact record after future inquiries during
those turns, not background jobs or autonomous periodic research.
Record only repository/tool facts, useful project associations, proposals and
rejection reasons; omit credentials and unrelated personal details.

## Read with bounded cost

1. Resolve the current catalog identity/version. Do not use an old download as authoritative.
2. Materialize it using the storage skill's normal route. Parsing a local JSON file
   does not require inserting its full contents in model context.
3. Run `python3 scripts/catalog.py query PATH --query "target capabilities project goal"`.
   Default: return at most 5 matching records and at most 12000 characters of record data.
   Ranking is deterministic lexical matching, not exhaustive semantic search.
4. Inspect the matched records; verify at most 3 relevant prior tools' material
   capability claims against current primary sources by default. The current
   target still requires its normal inspection.
5. Deliver the normal answer (direct fit plus up to 3 defensible unexpected combinations).
   If additional matches exist, the catalog exceeds 100 records, or a broader pass
   would exceed these limits, briefly offer a choice AFTER that useful answer:
   "I checked the most relevant saved tools. Want a broader pass for more examples?
   It will use more research and context."
6. Only with an explicit request for broader exploration use `--expanded --limit 15`
   (maximum 30000 record characters), verify more tools, or produce extra examples.
   Never dump or exhaustively compare the entire catalog by default, even after an
   expansion request; agree on a larger scope if necessary.
7. Respect "quick", "no history", a specific budget, or an existing explicit request
   for exhaustive exploration. Do not ask the same scope question again once answered.

These are workflow/context limits, not a hard token or dollar billing cap. Do not
invent a token price or imply retrieval sees every old chat. A large catalog alone
must not block the basic answer.

## Record format and writeback

Top level: `schema_version: 1`, `settings`, `updated_at`, `entries` array.
Each compact entry contains:
- `url`: canonical repository URL (deduplication key), `name`, `tags`;
- `last_inquiry_at`, `last_verified_at` (nullable), `revision` (nullable);
- `evidence_status`, `capabilities`, `interfaces`, `requirements`;
- `sources` (URLs), `project_relevance`, `inferred_ideas`, `rejected_ideas`;
- `provenance` and optional `history` summaries of material changes.

Keep the current record under about 200 words, excluding source URLs. Summarize;
do not copy chat transcripts. Historical inquiry titles with no inspected source
become `historical_unverified` leads, not established capability claims.
Do not add internal evaluation fixtures as the user's inquiries.

Use `python3 scripts/catalog.py upsert PATH --record RECORD.json` on the
fresh materialized file. The helper merges supplied fields by canonical URL and
preserves unrelated entries. Prepare the record from the current entry; retain
valuable prior proposals and rejection reasons in concise form.
Validate with `python3 scripts/catalog.py validate PATH`.
Replace the SAME durable file identity, using a retained version guard when available.
On a conflict, reread/re-materialize and reapply only this entry's change; never
overwrite others from a stale snapshot. Confirm a successful save before claiming
cross-chat persistence. A future host must have access to this file to use it.
