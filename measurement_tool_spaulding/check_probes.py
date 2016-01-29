# usage: python check_probes <lowercase_ISO_country_code>

import requests
import json
import sys

cc = sys.argv[1]

x = requests.get("https://atlas.ripe.net/api/v1/probe/?country_code=" + cc + "&fields=asn",)
data = json.loads(x.text)

probe_map = {}
f = open('probes_data.txt', 'w')
probe_data = data['objects']
for d in probe_data:
	if d['status_name'] == 'Connected':
		if str(d['asn_v4']) in probe_map:
			probe_map[str(d['asn_v4'])] += str(d['id'])
		else:
			probe_map[str(d['asn_v4'])] = [str(d['id'])]

for x in probe_map:
	f.write(x + ' ' + probe_map[x][0] + '\n')
	#f.write(str(d['id']) + ' ' + str(d['asn_v4']) + '\n')
f.close()
