import json

with open('old.json') as f:
  x = json.load(f)
  x = dict(map(lambda p: (p, x['data'][p]['version']), x['data'].keys()))

try:
  import in_place
  with in_place.InPlace('nginx/PKGBUILD', newline='') as f:
    for line in f:
      if line.startswith('pkgver'):
        line = 'pkgver=%s\n' % x['nginx']
      f.write(line)
except:
  pass
