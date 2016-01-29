import sys
import util

measurement_ids = ['3375736', '3375733', '3375761', '3375773', '3375774', '3375776', '3375777', '3375813', '3375846']

traceroutes = util.analyze_traceroute_measurements(measurement_ids)

ip_list = []
for t in traceroutes:
    for t2 in t:
        ip = t2.split(" ")[1]
#        if ip.split('.')[0].isdigit():
        ip_list.append(ip.strip())

#ip_list = []
#f = open(sys.argv[1], 'r')
#for line in f:
#    ip = line.split(" ")[1]
#    if ip.split('.')[0].isdigit():
#        ip_list.append(ip.strip())
#f.close()

ip_set = list(set(ip_list))
if '***' in ip_set:
    ip_set.remove('***')

f2 = open(sys.argv[1], 'w')
for ip in ip_set:
    f2.write(ip + '\n')
f2.close()
