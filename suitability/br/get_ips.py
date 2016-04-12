import sys
import re

file_list = [sys.argv[1]]
#file_list = ['relay_domain_brazil.txt', 'relay_domain_brazil-vps.txt', 'relay_domain_oregon.txt', 'relay_domain_ireland.txt', 'relay_domain_frankfurt.txt', 'relay_domain_tokyo.txt', 'relay_domain_seoul.txt', 'relay_domain_singapore.txt', 'relay_domain_singapore-vps.txt', 'relay_domain_sydney.txt', 'relay_domain_france.txt', 'relay_domain_spain.txt']
#file_list.append(sys.argv[1])

ips = []
for file_name in file_list:
    f = open(file_name, 'r')
    for line in f:
        if len(line.split(":")) == 1:
            if line.strip().split(" ")[0] != 'traceroute':
                pattern = r"\(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\)"
                pattern_re = re.compile(pattern)
                ip = pattern_re.findall(line.strip())
                if len(ip) > 0:
                    ip_addr = ip[0][1:-1].strip()
                    ips.append(ip_addr)
    f.close()

ips = list(set(ips))

f = open(sys.argv[2], 'w')
for i in ips:
    f.write(i + '\n')
f.close()
