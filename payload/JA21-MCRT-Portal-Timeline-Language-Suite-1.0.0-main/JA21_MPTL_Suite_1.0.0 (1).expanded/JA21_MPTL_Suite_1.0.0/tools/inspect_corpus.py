import gzip,json,collections,sys
p=sys.argv[1] if len(sys.argv)>1 else 'corpus/technical/JA21_MPTL_TECHNICAL_CORPUS_10000.jsonl.gz'
rows=[]
with gzip.open(p,'rt',encoding='utf-8') as f:
 for line in f: rows.append(json.loads(line))
print('records',len(rows))
print('classes',dict(collections.Counter(r['example_class'] for r in rows)))
print('tiers',dict(sorted(collections.Counter(r['tier'] for r in rows).items())))
print('topics',len(set(r['topic'] for r in rows)))
