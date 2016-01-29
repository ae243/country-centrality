import sys

ip_list = []
f = open(sys.argv[1], 'r')
for line in f:
    ip = line.split(" ")[1]
    if ip.split('.')[0].isdigit():
        ip_list.append(ip.strip())
f.close()

ip_set = list(set(ip_list))
if '***' in ip_set:
    ip_set.remove('***')

f2 = open(sys.argv[2], 'w')
for ip in ip_set:
    f2.write(ip + '\n')
f2.close()
