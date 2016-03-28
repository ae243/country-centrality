import sys
import re
import pycountry

# usage: python analyze_paths.py <client_cc> <avoid_cc> <ip_country_map> <xx_client_relay.txt>

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
not_suitable = []
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
            else:
                not_suitable.append(current_country_relay)
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
if not y in current_country_relay:
    non_y_relays += 1
co = pycountry.countries.get(alpha2=y)
if not co.name in current_trace:
    suitable_relays += 1
else:
    not_suitable.append(current_country_relay)
total_relays += 1
f.close()

print suitable_relays
print non_y_relays
print not_suitable

# second analyze paths from all "suitable" relays to all domains
# right now this is manual - you have to manually remove the files that are not necessary according to the first step
file_list = ['relay_domain_brazil.txt', 'relay_domain_brazil-vps.txt', 'relay_domain_oregon.txt', 'relay_domain_ireland.txt', 'relay_domain_frankfurt.txt', 'relay_domain_tokyo.txt', 'relay_domain_seoul.txt', 'relay_domain_singapore.txt', 'relay_domain_singapore-vps.txt', 'relay_domain_sydney.txt', 'relay_domain_france.txt', 'relay_domain_spain.txt']

suitable_paths = 0
total_paths = 0
current_trace = []
for file_name in file_list:
    f = open(file_name, 'r')
    for line in f:
        if line.split(" ")[0] == 'traceroute':
            if current_trace != []:
                #analyze path
                co = pycountry.countries.get(alpha2=y)
                if not co.name in current_trace:
                    suitable_paths += 1
                total_paths += 1
            current_trace = []
        else:
            pattern = r"\(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\)"
            pattern_re = re.compile(pattern)
            ip = pattern_re.findall(line.strip())
            if len(ip) > 0:
                ip_addr = ip[0][1:-1].strip()
                cc = ip_country[ip_addr]
                current_trace.append(cc)
co = pycountry.countries.get(alpha2=y)
if not co.name in current_trace:
    suitable_paths += 1
total_paths += 1

print suitable_paths
print total_paths

suitability = (float(suitable_relays)/float(non_y_relays))*(float(suitable_paths)/float(total_paths))
print suitability
