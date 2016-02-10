import sys

ip_list = []
f = open(sys.argv[1], 'r')
for line in f:
    ip = line.split(" ")[1]
    if ip.split('.')[0].isdigit():
        ip_list.append(ip.strip())
f.close()

f2 = open(sys.argv[2], 'r')
for line in f2:
    ip = line.split(" ")[1]
    if ip.split('.')[0].isdigit():
        ip_list.append(ip.strip())
f2.close()

f3 = open(sys.argv[3], 'r')
for line in f3:
    ip = line.split(" ")[1]
    if ip.split('.')[0].isdigit():
        ip_list.append(ip.strip())
f3.close()

f4 = open(sys.argv[4], 'r')
for line in f4:
    ip = line.split(" ")[1]
    if ip.split('.')[0].isdigit():
        ip_list.append(ip.strip())
f4.close()

ip_set = list(set(ip_list))
if '***' in ip_set:
    ip_set.remove('***')

f5 = open('traceroute_ips.txt', 'w')
for ip in ip_set:
    f5.write(ip + '\n')
f5.close()
