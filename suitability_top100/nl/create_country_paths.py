import sys
import pycountry
import re

# usage: python create_country_paths.py <ip_country_mapping> <traceroute_file> <result_file_name> 

f = open(sys.argv[1], 'r')
ip_map = {}
for line in f:
    items = line.split(",")
    if len(items) < 2:
        ip = line.split(" ")[0]
        cc = 'None'
    else:
        ip = items[0]
        cc = items[1]
    ip_map[ip] = cc
f.close()

f_res = open(sys.argv[3], 'w')
f = open(sys.argv[2], 'r')
current_trace = ''
for line in f:
    if line.split(" ")[0] == 'traceroute':
        # write current trace
        f_res.write(current_trace + '\n')
        current_trace = line.split(" ")[2]
    else:
        pattern = r"\(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\)"
        pattern_re = re.compile(pattern)
        ip = pattern_re.findall(line.strip())
        if len(ip) > 0:
            ip_addr = ip[0][1:-1].strip()
            cc = ip_map[ip_addr]
            current_trace += '|'
            current_trace += str(cc)
f_res.write(current_trace + '\n')
f.close()
f_res.close()
