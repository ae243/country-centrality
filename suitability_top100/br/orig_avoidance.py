import sys
import re
import pycountry

# usage: python orig_avoidance.py <client_cc> <avoid_cc> <ip_map> <country_path_file>

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

domain_map = {}
domain_exist = {}
current_trace = []
file_list = [sys.argv[4]]
for file_name in file_list:
    f = open(file_name, 'r')
    for line in f:
        if len(line.split("|")) > 1:
            domain = line.split("|")[0]
            if not domain in domain_map:
                countries = line.strip().split("|")[1:]
                co = pycountry.countries.get(alpha2=y)
                if not co.name in countries:
                    domain_map[domain] = 1
                    print domain, countries
            domain_exist[domain] = 1
    f.close()

total_avoidable = len(domain_map)
total = len(domain_exist)
print total_avoidable
print total
print float(total_avoidable)/float(total)
