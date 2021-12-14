import json
import sys
from jsonmerge import merge

db = {}

for f in sys.argv[1:]:
    print('Keys for "{}": {}'.format(f, json.load(open(f)).keys()), file=sys.stderr)

    d = json.load(open(f))

    if 'wish-list' in f:
        db['wish-list-users'] = d['users']

    if 'online-store' in f:
        db['online'] = d
    elif 'physical-store' in f:
        db['physical'] = d
    else:
        db = merge(db, d)

print(json.dumps(db))
