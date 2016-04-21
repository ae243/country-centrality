import sys
import re

file_map = {'asymmetry_AU.txt': '52.63.71.83', 'asymmetry_US.txt': '52.38.239.20', 'asymmetry_IE.txt': '52.50.199.45', 'asymmetry_DE.txt': '52.58.44.37', 'asymmetry_JP.txt': '52.196.116.106', 'asymmetry_KR.txt': '52.79.174.41', 'asymmetry_SG.txt': '54.179.145.21', 'asymmetry_BR.txt': '52.67.34.34'}

f = open('new_asymmetry_ips_mm.txt', 'r')
ip_map = {}
for line in f:
    items = line.strip().split(",")
    if len(items) > 1:
        ip = items[0]
        cc = items[1]
        ip_map[ip] = cc
    else:
        ip = line.strip().split(" ")[0]
        cc = 'None'
        ip_map[ip] = cc
f.close()

f_res = open('cc_paths.txt', 'w')
for file_name in file_map:
    f = open(file_name, 'r')
    current_trace = ''
    current_from = file_map[file_name]
    current_to = ''
    for line in f:
        if line.split(" ")[0] == 'traceroute':
            f_res.write(current_from + "|" + current_to + current_trace + "\n")
            current_trace = ''
            current_to = line.split(" ")[2].strip()
        else:
            pattern = r"\(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\)"
            pattern_re = re.compile(pattern)
            ip = pattern_re.findall(line.strip())
            if len(ip) > 0:
                ip_addr = ip[0][1:-1].strip()
                current_trace += '|' + ip_map[ip_addr]
    f_res.write(current_from + "|" + current_to + current_trace + "\n")
    f.close()

f = open(sys.argv[1], 'r')
current_trace = []
current_from = ''
current_to = ''
for line in f:
    if line.split(":")[0] == '1':
        f_res.write(current_from + "|" + current_to + current_trace + "\n")
        current_trace = ''
        current_to = ''
    else:
        ip_addr = line.split(" ")[1].strip()
        current_trace += '|' + ip_map[ip_addr]
f_res.write(current_from + "|" + current_to + current_trace + "\n")
f.close()
f_res.close()
