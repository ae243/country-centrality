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
