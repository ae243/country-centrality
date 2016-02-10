import sys
import ipaddr
import netaddr

f = open('all_probes.txt', 'r')
l = []
for line in f:
    l.append(line.split(" ")[1].strip())
f.close()

subnet_map = {} # map of <subnet, list of IPs in subnet>
for ip in l:
	x = netaddr.IPNetwork(ip)
	real_sub = x.supernet(24)[0]
	if real_sub in subnet_map:
		subnet_map[real_sub] += ip
	else:
		subnet_map[real_sub] = [ip]

print len(l)
print len(subnet_map)
f_res = open('subnets.txt', 'w')
for s in subnet_map:
	f_res.write(str(s) + "\n")
f_res.close()
