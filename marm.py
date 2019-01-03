import ujson
import hashlib


doc = dict(a=1, b=2, c=3)
doc['d'] = dict(doc)

s = ujson.dumps(doc, sort_keys=True)
b = bytes(s, 'utf-8')
m = hashlib.sha256()
m.update(b)
h = m.hexdigest()
