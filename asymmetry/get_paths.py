import sys
import util

f_map = open(sys.argv[1], 'r')
country_map = {}
for line in f_map:
    ip = line.split(" ")[0]
    country = line.split(" ")[3].strip()
    country_map[ip] = country

country_map['201.48.44.186'] = 'BR'
country_map['198.32.124.176'] = 'US'
country_map['72.52.92.53'] = 'US'
country_map['184.105.213.70'] = 'US'
country_map['184.105.223.166'] = 'US'
country_map['72.52.92.165'] = 'US'
country_map['72.52.92.221'] = 'US'
country_map['89.185.139.151'] = 'IE'
country_map['89.185.136.1'] = 'IE'

measurement_ids = ['3375771']

traces = util.analyze_traceroute_measurements(measurement_ids)

new_traces = []
for t in traces:
    new_t = []
    for ip in t:
        ip_addr = ip.split(" ")[1]
        new_t.append(ip_addr)
    new_traces.append(new_t)

germany_paths = []
for t in new_traces:
    country_path = []
    for ip in t:
        if ip.strip() != '***':
            country_path.append(country_map[ip])
    germany_paths.append(country_path)

for g in germany_paths:
    print g
