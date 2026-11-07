"""Offline integrity checks. Does not certify legal accuracy or remote URL availability."""
from pathlib import Path
from datetime import date
from urllib.parse import unquote
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
def main():
    errors=[]
    sources=json.loads((ROOT/'config/sources.json').read_text())
    date.fromisoformat(sources['reviewed_at'])
    ids=[s['id'] for s in sources['sources']]
    if len(ids)!=len(set(ids)):errors.append('Duplicate source IDs')
    for s in sources['sources']:
        if not s['url'].startswith('https://'):errors.append(f'Invalid source URL {s["id"]}')
        if not s['evidence'].strip():errors.append(f'Missing evidence {s["id"]}')
    for p in ROOT.rglob('*.json'):
        try:json.loads(p.read_text())
        except Exception as exc:errors.append(f'{p.relative_to(ROOT)}: {exc}')
    for p in ROOT.rglob('*.md'):
        text=p.read_text()
        if not text.strip():errors.append(f'Empty {p}')
        if len(re.findall(r'^```',text,re.M))%2:errors.append(f'Unclosed fence {p}')
        outside=re.sub(r'^```.*?^```\s*$', '', text, flags=re.M|re.S)
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',outside):
            target=target.strip().split(' "')[0]
            if re.match(r'^[a-zA-Z]+:',target) or target.startswith('#'):continue
            local=unquote(target.split('#')[0])
            if local and not (p.parent/local).exists():errors.append(f'Broken link: {p.relative_to(ROOT)} -> {target}')
        if 'docs' in p.relative_to(ROOT).parts:
            for sid in set(re.findall(r'\bS\d{2}\b',text)):
                if sid not in ids:errors.append(f'Unknown source {sid} in {p}')
    catalog=json.loads((ROOT/'config/catalog.json').read_text())
    listed={page['path'] for cat in catalog for page in cat['pages']}
    actual={p.relative_to(ROOT).as_posix() for p in (ROOT/'docs').rglob('*.md') if p.name!='README.md'}
    if actual != listed:errors.append(f'Catalog mismatch: {actual ^ listed}')
    for cat in catalog:
        if not cat['pages']:errors.append(f'Empty category {cat["category"]}')
    skills=list((ROOT/'skills').glob('*/SKILL.md'))
    for p in skills:
        m=re.match(r'^---\nname: ([a-z0-9-]{1,63})\ndescription: "([^\n]+)"\n---\n',p.read_text())
        if not m or m.group(1)!=p.parent.name:errors.append(f'Invalid skill metadata {p}')
    rules=json.loads((ROOT/'config/training-rules.json').read_text())
    if rules['purpose']!='TRAINING_ONLY_NOT_APPROVED_FOR_PRODUCTION':errors.append('Training rules missing scope guard')
    for venue in rules['markets']:
        if not set(venue['source_ids']) <= set(ids):errors.append('Unknown rule source')
    if errors:
        print('\n'.join(errors));return 1
    print(f'PASS: {len(actual)} indexed pages, {len(catalog)} categories, {len(ids)} sources, {len(skills)} skills; local links/JSON/fences valid')
    return 0
if __name__=='__main__':sys.exit(main())
