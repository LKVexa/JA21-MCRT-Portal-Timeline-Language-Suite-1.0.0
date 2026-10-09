from pathlib import Path
import gzip,json,csv,hashlib,collections,sys,zipfile
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def h(b): return hashlib.sha256(b).hexdigest()
# corpus
cp=ROOT/'corpus/technical/JA21_MPTL_TECHNICAL_CORPUS_10000.jsonl.gz'
rows=[]
with gzip.open(cp,'rt',encoding='utf-8') as f:
    for line in f: rows.append(json.loads(line))
if len(rows)!=10000: errors.append(f'corpus_count={len(rows)}')
if len({r['source_record_id'] for r in rows})!=10000: errors.append('duplicate corpus IDs')
for r in rows:
    if h(r['source'].encode())!=r['source_hash'].split(':',1)[-1]: errors.append('source hash '+r['source_record_id']);break
if len(set(r['topic'] for r in rows))!=45: errors.append('topic coverage')
# scripts/catalog
scripts=sorted(ROOT.glob('scripts/**/*.mcrt'))
if len(scripts)!=1000: errors.append(f'script_count={len(scripts)}')
with open(ROOT/'catalogs/SCRIPT_CATALOG.csv',encoding='utf-8') as f: cat=list(csv.DictReader(f))
if len(cat)!=1000: errors.append(f'catalog_count={len(cat)}')
if collections.Counter(x['example_class'] for x in cat)!=collections.Counter({'positive':788,'negative':142,'certification':70}): errors.append('script class composition')
if collections.Counter(int(x['tier']) for x in cat)!=collections.Counter({1:100,2:150,3:250,4:250,5:150,6:100}): errors.append('tier composition')
if len(set(x['topic'] for x in cat))!=45: errors.append('script topic coverage')
for x in cat:
    p=ROOT/x['script_path']
    if not p.exists(): errors.append('missing '+x['script_path']);break
    if 'mcrt portal.timeline 0.3' not in p.read_text(encoding='utf-8'): errors.append('header '+x['script_path']);break
    if 'policy no_network' not in p.read_text(encoding='utf-8'): errors.append('policy '+x['script_path']);break
    if 'sha256:'+h(p.read_bytes())!=x['script_hash']: errors.append('script hash '+x['script_path']);break
# textbook
book=(ROOT/'textbook/JA21_MCRT_PORTAL_TIMELINE_LANGUAGE_TEXTBOOK.md').read_text(encoding='utf-8')
if book.count('\n## Chapter ')!=22: errors.append('textbook chapters')
# paths
mx=max(len(str(p.relative_to(ROOT))) for p in ROOT.rglob('*'))
if mx>120: errors.append(f'max path {mx}')
print(json.dumps({'status':'PASS' if not errors else 'FAIL','errors':errors,'corpus':len(rows),'scripts':len(scripts),'catalog':len(cat),'topics':len(set(r['topic'] for r in rows)),'max_relative_path':mx},indent=2))
sys.exit(1 if errors else 0)
