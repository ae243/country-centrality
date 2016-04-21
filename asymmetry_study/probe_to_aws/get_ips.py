import sys

f = open(sys.argv[1], 'r')
ips = []
for line in f:
    ip = line.split(" ")[1]
    ips.append(ip)
f.close()

ips = list(set(ips))

f = open(sys.argv[2], 'w')
for i in ips:
    f.write(i + '\n')
f.close()
