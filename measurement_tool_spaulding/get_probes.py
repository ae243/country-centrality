# usage: python get_probes <lowercase_ISO_country_code>

import requests
import json
import sys

cc = sys.argv[1]

x = requests.get("https://atlas.ripe.net/api/v1/probe/?country_code=" + cc,)
data = json.loads(x.text)

f = open('probes.txt', 'w')
probe_data = data['objects']
for d in probe_data:
	f.write(str(d['id']) + '\n')
f.close()
