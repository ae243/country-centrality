import sys
import re
import pycountry

# usage: python analyze_paths.py <client_cc> <avoid_cc> <ip_map> <xx_client_relay.txt>

ip_country = {}
f = open(sys.argv[3], 'r')
for line in f:
    ip = line.split(",")[0].strip()
    if len(line.split(",")) > 1:
        country = line.split(",")[1].strip()
    else:
        ip = line.split(" ")[0].strip()
        country = 'None'
    ip_country[ip] = country
f.close()

# x is the country that the client is in
x = sys.argv[1]

# y is the country code that the client wants to avoid
y = sys.argv[2]

# first analyze paths from client to all relays
total_relays = 0
suitable_relays = 0
suitable = []
non_y_relays = 0
f = open(sys.argv[4], 'r')
current_trace = []
current_country_relay = ''
for line in f:
    if line.split(":")[0] == 'CC':
        # analyze last trace
        if current_country_relay != '' and current_trace != []:
            if not y in current_country_relay:
                non_y_relays += 1
            co = pycountry.countries.get(alpha2=y)
            if not co.name in current_trace and (not y in current_country_relay):
                suitable_relays += 1
                suitable.append(current_country_relay)
            total_relays += 1
        current_country_relay = line.split(":")[1].strip()
        current_trace = []
    elif line.split(" ")[0] != 'traceroute':
        pattern = r"\(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\)"
        pattern_re = re.compile(pattern)
        ip = pattern_re.findall(line.strip())
        if len(ip) > 0:
            ip_addr = ip[0][1:-1].strip()
            cc = ip_country[ip_addr]
            current_trace.append(cc)
#analyze the last trace
if current_country_relay != '' and current_trace != []:
    if not y in current_country_relay:
        non_y_relays += 1
    co = pycountry.countries.get(alpha2=y)
    if not co.name in current_trace:
        suitable_relays += 1
        suitable.append(current_country_relay)
    total_relays += 1
f.close()

print suitable_relays
print non_y_relays
print suitable

file_map = {'BR-AWS': 'cc_brazil.txt', 'BR-VPS': 'cc_brazil-vps.txt', 'SG-AWS': 'cc_singapore.txt', 'SG-VPS': 'cc_singapore-vps.txt', 'US': 'cc_oregon.txt', 'FR': 'cc_france.txt', 'ES': 'cc_spain.txt', 'IE': 'cc_ireland.txt', 'DE': 'cc_frankfurt.txt', 'JP': 'cc_tokyo.txt', 'KR': 'cc_seoul.txt', 'AU': 'cc_sydney.txt'}

domain_endpoint = {}
for file_name in file_map.values():
    f = open('filter_' + file_name, 'r')
    for line in f:
        domain = line.split("|")[0]
        if domain in domain_endpoint:
            end = line.strip().split("|")[-1]
            domain_endpoint[domain].append(end)
        else:
            end = line.strip().split("|")[-1]
            domain_endpoint[domain] = [end]

upper = 0.0
for d in domain_endpoint:
    ends = list(set(domain_endpoint[d]))
    if len(ends) == 1:
        co = pycountry.countries.get(alpha2=y)
        if ends[0] == co.name:
            upper += 1.0
            print d

print upper
upper = 1.0 - (upper/len(domain_endpoint))
print "Upper: " + str(upper)

domain_map = {}
domain_exist = {}
current_trace = []
file_list = [file_map[z] for z in suitable]
for file_name in file_list:
    f = open('filter_' + file_name, 'r')
    for line in f:
        domain = line.split("|")[0]
        if not domain in domain_map:
            countries = line.strip().split("|")[1:]
            co = pycountry.countries.get(alpha2=y)
            if not co.name in countries:
                domain_map[domain] = 1
        domain_exist[domain] = 1
    f.close()

temp = list(set(domain_exist.keys()) - set(domain_map.keys()))
print temp

total_avoidable = len(domain_map)
total = len(domain_exist)
print total_avoidable
print total
print float(total_avoidable)/float(total)
