import subprocess
import sys

f = open('all_probes.txt', 'r')
ips = []
id_ip = {}
for line in f:
    id = line.split(" ")[0].strip()
    ip = line.split(" ")[1].strip()
    id_ip[id] = ip
    ips.append(ip)
f.close()

'''
f_netcat_query = open('netcat_query.txt', 'w')
f_netcat_query.write('begin\n')
f_netcat_query.write('verbose\n')
for p in ips:
    f_netcat_query.write(p + '\n')
f_netcat_query.write('end\n')
f_netcat_query.close()

command = ('netcat whois.cymru.com 43 < netcat_query.txt | sort -n > netcat_lookup.txt')
r = subprocess.Popen(command, shell=True)
r.wait()
'''

asn_ip = {}
f_as = open('netcat_lookup.txt', 'r')
for line in f_as:
    asn = line.split("|")[0].strip()
    ip = line.split("|")[1].strip()
    asn_ip[ip] = asn
f_as.close()

id_asn = {} # <ID, ASN>
for id in id_ip:
    ip = id_ip[id]
    asn = asn_ip[ip]
    id_asn[id] = asn

f_res = open('probe_id_asn.txt', 'w')
for x in id_asn:
    f_res.write(x + " " + id_asn[x] + "\n")
f_res.close()
