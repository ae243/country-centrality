import sys
from netaddr import IPNetwork, IPAddress

ips = []
f = open('dns_ips.txt', 'r')
for line in f:
    ips.append(line.strip())
f.close()

ips = list(set(ips))

subnets = []
f2 = open('subnets.txt', 'r')
for line in f2:
    subnets.append(line.strip())
f2.close()

subnets = list(set(subnets))

count = 1
f_found = open('covered_ips.txt', 'w')
f_notfound = open('uncovered_ips.txt', 'w')
for i in ips:
    print str(count) + "/" + str(len(ips))
    found = False
    for s in subnets:
        if IPAddress(i) in IPNetwork(s):
            found = True
            f_found.write(i + '\n')
            break
    if found == False:
        f_notfound.write(i + '\n')
    count += 1
f_found.close()
f_notfound.close()
