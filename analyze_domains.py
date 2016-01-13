import sys

def clean_targets(targets):
    clean = []
    for t in targets:
        if t[0:4] == 'http':
            t = t[8:]
        if t[0:5] == 'https':
            t = t[9:]
        clean.append(t.split("/")[0])
    return clean

f = open(sys.argv[1], 'r')
domain_map = {}
url_map = {}
for line in f:
    items = line.strip().split(',')
    subdomains = list(set(clean_targets(items[1:-1])))
    num_subdomains = len(subdomains)
    if num_subdomains in domain_map:
        domain_map[num_subdomains] += 1
        url_map[num_subdomains].append(items[0])
    else:
        domain_map[num_subdomains] = 1
        url_map[num_subdomains] = [items[0]]

for d in domain_map:
    print d, domain_map[d]
    if d > 10:
        print url_map[d]
