import util
import sys

f = open(sys.argv[1], 'r')
domains = []
for line in f:
    d = line.split(',')[:-1]
    for u in d:
        domains.append(u.strip())
f.close()

cleaned_domains = list(set(util.clean_targets(domains)))

f_res = open(sys.argv[2], 'w')
for c in cleaned_domains:
    f_res.write(c + "\n")
f_res.close()
