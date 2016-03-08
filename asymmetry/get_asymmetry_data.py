import sys
import util
import requests
import json

'''
# get map of probe id to ip address
x = requests.get("https://atlas.ripe.net/api/v1/probe/")
data = json.loads(x.text)
probe_data = data['objects']

probe_map = {}
offset = 100
while len(probe_data) > 0:
    for d in probe_data:
        probe_map[d['id']] = d['address_v4']
    x = requests.get("https://atlas.ripe.net/api/v1/probe/?offset=" + str(offset),)
    data = json.loads(x.text)
    probe_data = data['objects']
    offset += 100
'''

# get map of <ip address -> country>
f = open('asymmetry_latest_mm.txt', 'r')
ip_map = {}
for line in f:
    ip = line.split(" ")[0].strip()
    cc = line.split(" ")[3].strip()
    ip_map[ip] = cc
f.close()

# get map of <(start_ip, dest_ip) -> [country level paths]>
path_map = {}
f = open('measurementids.txt', 'r')
count = 1
for line in f:
    print "COUNT: " + str(count) + "/4065"
    try:
        s_d = util.get_start_dest_traceroute([line.strip()])
        path_map.update(s_d)
    except:
        print "ERROR"
    count += 1
f.close()

f_res = open('asymmetry_results_log.txt', 'w')
count = 0
symm = 0
asymm = 0
for x in path_map:
    (s,d) = x
    if (d,s) in path_map:
        forward = path_map[x]
        reverse = path_map[(d,s)]
        # convert forward and reverse to country-level and remove N/A and duplicates that are consecutive
        country_forward = []
        country_reverse = []
        for f in forward:
            current_cc = ip_map[f.split(" ")[1].strip()]
            if current_cc != 'N/A' and len(country_forward) == 0:
                country_forward.append(current_cc)
            elif current_cc != 'N/A' and len(country_forward) > 0 and current_cc != country_forward[-1]:
                country_forward.append(current_cc)
        for r in reverse:
            current_cc = ip_map[r.split(" ")[1].strip()]
            if current_cc != 'N/A' and len(country_reverse) == 0:
                country_reverse.append(current_cc)
            elif current_cc != 'N/A' and len(country_reverse) > 0 and current_cc != country_reverse[-1]:
                country_reverse.append(current_cc)
        if country_forward == list(reversed(country_reverse)):
            f_res.write(str(country_forward) + " " + str(country_reverse) + "\n")
            symm += 1
        else:
            f_res.write(str(country_forward) + " " + str(country_reverse) + "\n")
            asymm += 1
        count += 1

f_res.write("Symmetric: " + str(symm) + "\n")
f_res.write("Asymmetric: " + str(asymm) + "\n")
f_res.write("Total: " + str(count) + "\n")
f_res.close()
