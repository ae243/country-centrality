import sys
import re
import subprocess

f = open('final_resolvers.txt', 'r')
resolver_list = []
for line in f:
    resolver = line.split(",")[0].strip()
    resolver_list.append(resolver)
f.close()

ip_list = []
f = open(sys.argv[1], 'r')
for line in f:
    items = line.strip().split(",")
    if items[0] in resolver_list and len(items) > 1:
        resps = ",".join(items[1:])
        ips = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", resps)
        ip_list.extend(ips)
f.close()
print len(ip_list)

ip_set = list(set(ip_list))
print len(ip_set)
