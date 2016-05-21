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

ip_set = list(set(ip_list))
f_res = open('us_open_resolver_traces.txt', 'w')
# run trace to every IP and record destIP, trace
for ip in ip_set:
    traceroute = subprocess.Popen(["traceroute", ip],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    traceroute.wait()
    for line in iter(traceroute.stdout.readline,""):
        f_res.write(line)
f_res.close()
