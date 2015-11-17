import sys
import os
import subprocess

f = open(sys.argv[1], 'r')
f2 = open(sys.argv[2], 'w')

f3 = open('netcat_temp.txt', 'w')
f3.write('begin\n')
f3.write('verbose\n')

ip_list = []
for line in f:
	if line[0] != '#' and len(line.split(':')[1].strip().split(' ')) >= 2:
		ip = line.split(':')[1].strip().split(' ')[0].strip()
		if not ip in ip_list:
			f3.write(ip + '\n')
			ip_list.append(ip)
f3.write('end\n')
f3.close()
f.close()

command = ('netcat whois.cymru.com 43 < netcat_temp.txt | sort -n > list02')
r = subprocess.Popen(command, shell=True)
r.wait()
f_temp = open('list02', 'r')
ip_country_map = {}
ip_as_map = {}
for line in f_temp:
	items = line.split('|')
	if len(items) > 1:
		ip_country_map[items[1].strip()] = items[3].strip()
		ip_as_map[items[1].strip()] = items[0].strip()
f_temp.close()

f = open(sys.argv[1], 'r')
for line in f:
	hop = line.split(':')[0].strip()
	if line[0] == '#':
		new_line = line
	elif len(line.split(':')[1].strip().split(' ')) < 2:
		new_line = line
	else:
		ip = line.split(':')[1].strip().split(' ')[0].strip()
		rtt = line.split(':')[1].strip().split(' ')[1].strip()
		if ip in ip_country_map:
			country = ip_country_map[ip]
			asn = ip_as_map[ip]
			new_line = hop + ": " + ip + " " + rtt + " " + str(country) + " " + str(asn) + "\n"
		else:
			new_line = line
	f2.write(new_line)
f.close()
f2.close()
