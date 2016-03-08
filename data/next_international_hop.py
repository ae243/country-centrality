import sys

def analyze_country(cc):
    total_paths = 0
    hosted = 0
    transit = 0
    for p in paths:
        if p[-1].strip() == cc:
            hosted += 1
        elif cc in p:
            transit += 1
    return [hosted, transit]

paths = []
f = open(sys.argv[1], 'r')
for line in f:
    items = line.split(" ")
    new_items = []
    for i in items:
        if i != 'N/A':
            new_items.append(i.strip())
    if 'BR' in new_items:
        paths.append(new_items)

print len(paths)

new_paths = []
for p in paths:
    n = []
    for p2 in p:
        if p2 != 'N/A':
            n.append(p2)
    new_paths.append(n)

next_map = {}
for n in new_paths:
    need_next = False
    for n2 in n:
        if n2 == 'BR' and need_next == False:
            need_next = True
        elif n2 != 'BR' and need_next == True:
            if n2 in next_map:
                next_map[n2] += 1
            else:
                next_map[n2] = 1
            need_next = False

for n in next_map:
    print n, next_map[n]

'''
countries = []
for p in paths:
    countries.extend(p)

unique_countries = list(set(countries))
if 'N/A' in unique_countries:
    unique_countries.remove('N/A')
print len(unique_countries)

f_res = open('results.txt', 'w')
for u in unique_countries:
    [h, t] = analyze_country(u)
    print u
    print "Hosted: " + str(h)
    print "Transits: " + str(t)
f_res.close()
'''
