import sys

f = open('total_domains.txt', 'r')
domains = []
for line in f:
    items = line.split(",")
    domain_list = items[:-2]
    domains.extend(domain_list)
f.close()
print len(domains)
unique_domains = list(set(domains))
print len(unique_domains)
f_res = open('domains.txt', 'w')
for u in unique_domains:
    f_res.write(u + '\n')
f_res.close()
