import json,io
f = io.open("info.json", encoding='utf-8')
info = json.load(f)
i=len(info['class'])
print i
