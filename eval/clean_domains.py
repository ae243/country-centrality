import util
import sys

f = open('domains.txt', 'r')
domains = []
for line in f:
    domains.append(line.strip())
f.close()

cleaned_domains = list(set(util.clean_targets(domains)))

f_res = open('cleaned_domains.txt', 'w')
for c in cleaned_domains:
    f_res.write(c + "\n")
f_res.close()
