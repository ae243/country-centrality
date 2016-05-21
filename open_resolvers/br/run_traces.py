import sys

ip_list = []
f = open(sys.argv[1], 'r')
    for line in f:
        items = line.strip().split(",")
        ips = items[]
        ip_list.extend(ips)
f.close()

# run trace to every IP and record destIP, trace
for ip in ip_list:
    # run trace
