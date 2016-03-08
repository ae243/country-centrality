import sys
import util
import requests
import json

# get all ip addresses
ip_list = []
f = open('measurementids.txt', 'r')
for line in f:
    t_list = util.analyze_traceroute_measurements([line.strip()])
    for t in t_list:
        for t2 in t:
            ip_list.append(t2.split(" ")[1])
f.close()

ip_list = list(set(ip_list))
print len(ip_list)

f2 = open('ips.txt', 'w')
for ip in ip_list:
    f2.write(ip + "\n")
f2.close()
