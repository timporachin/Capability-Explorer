"""Dependency-free structural checks; does not evaluate model behavior."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    skill = root / 'skills/capability-explorer/SKILL.md'
    required = [skill, root / 'README.md', root / 'LICENSE',
                root / 'VERSION', root / 'tests/acceptance.md',
                root / 'INSTALL.md', root / 'CONTRIBUTING.md',
                root / 'examples/README.md', root / 'launch/README.md',
                root / 'tests/RESULTS.md']
    for path in required:
        if not path.is_file():
            errors.append(f'Missing: {path.relative_to(root)}')
    if errors:
        return errors
    text = skill.read_text(encoding='utf-8')
    frontmatter = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not frontmatter:
        errors.append('Missing YAML frontmatter')
    else:
        fields = dict(re.findall(r'^([a-z-]+): (.+)$', frontmatter[1], re.M))
        if set(fields) != {'name', 'description'}:
            errors.append('Frontmatter must contain name and description')
        if fields.get('name') != 'capability-explorer':
            errors.append('Skill name differs from folder name')
        if len(fields.get('description', '')) < 40:
            errors.append('Description lacks trigger context')
    if len(text.splitlines()) >= 500:
        errors.append('Skill exceeds the concise package limit')
    if root.joinpath('VERSION').read_text().strip() != '0.1.0':
        errors.append('Unexpected version')
    for doc in root.rglob('*.md'):
        content = doc.read_text(encoding='utf-8')
        if re.search(r'\bTODO\b|\{=html\}', content):
            errors.append(f'Unfinished/export artifact: {doc.relative_to(root)}')
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            if re.match(r'[a-z]+://|#', link):
                continue
            target = doc.parent / link.split('#')[0]
            if not target.exists():
                errors.append(f'Broken link in {doc.relative_to(root)}: {link}')
    return errors


if __name__ == '__main__':
    errors = validate()
    if errors:
        print('\n'.join(errors))
        raise SystemExit(1)
    print('PASS: v0.1 package structure, metadata, version, and local links')
