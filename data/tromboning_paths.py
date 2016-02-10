import sys

def find_tromboning(paths):
    trombone_count = 0
    other_countries = {}
    for p in paths:
        if p[-1].strip() == 'BR' and p[0].strip() == 'BR' and len(set(p)) > 1:
            trombone_count += 1
            for c in list(set(p)):
                if c.strip() != 'BR':
                    if c.strip() in other_countries:
                        other_countries[c.strip()] += 1
                    else:
                        other_countries[c.strip()] = 1
    print "# of Tromboning paths: " + str(trombone_count) + "\n"
    for o in other_countries:
        print o + ": " + str(other_countries[o]) + "\n"

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

find_tromboning(paths)
