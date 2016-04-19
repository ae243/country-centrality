# usage: python check_probes <lowercase_ISO_country_code>

import requests
import json
import sys

x = requests.get("https://atlas.ripe.net/api/v1/probe/?fields=address_v4",)
data = json.loads(x.text)

probe_map = {}
f = open('probes_data.txt', 'w')
probe_data = data['objects']
for d in probe_data:
	if d['status_name'] == 'Connected':
	    probe_map[str(d['id'])] += str(d['id'])
		else:
			probe_map[str(d['asn_v4'])] = [str(d['id'])]

for x in probe_map:
	f.write(x + ' ' + probe_map[x][0] + '\n')
f.close()
