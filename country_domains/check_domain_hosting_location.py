import sys

f = open(sys.argv[1], 'r')
domain_host = {}
for line in f:
    domain = line.split("|")[0].strip()
    host = line.split("|")[-1].strip()
    domain_host[domain] = host
f.close()

f = open(sys.argv[2], 'r')
host_map = {}
for line in f:
    if line.strip() in domain_host:
        c = domain_host[line.strip()]
        if c in host_map:
            host_map[c] += 1
        else:
            host_map[c] = 1
    else:
        print line.strip() + " not in traceroutes"
f.close()

for x in host_map:
    print x, host_map[x]
