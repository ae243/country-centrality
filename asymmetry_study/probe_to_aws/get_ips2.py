import sys
import re

file_list = sys.argv[1:-1]

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

f = open(sys.argv[-1], 'w')
for i in ips:
    f.write(i + '\n')
f.close()
