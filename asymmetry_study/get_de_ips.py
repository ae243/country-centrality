import sys

f = open(sys.argv[1], 'r')
f_res = open('digital_envoy_ips.txt', 'w')
for line in f:
    ip = line.split(":")[0].strip()
    f_res.write(ip + '\n')
f.close()
f_res.close()
