import sys

f_c = open('client_relay_mm.txt', 'r')
ip_map = {}
for line in f_c:
    ip = line.split(" ")[0].strip()
    cc = line.split(" ")[3].strip()
    ip_map[ip] = cc
f_c.close()

print ip_map

f_res = open('client_relay_country.txt', 'w')
f = open('client_relay_processed.txt', 'r')
for line in f:
    cc = line.split("|")[0].strip()
    ips = line.strip().split("|")[1:]
    c_list = []
    for ip in ips:
        country = ip_map[ip]
        c_list.append(country.strip())
    new_line = cc + "|" + "|".join(c_list)
    f_res.write(new_line + "\n")
f.close()
f_res.close()
