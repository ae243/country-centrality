import sys

total_tromboning = 0
domestic_traffic = 0
total_paths = 0
t_map = {}
f = open(sys.argv[1], 'r')
for line in f:
    items = line.strip().split("|")
    domain = items[0]
    countries = items[1:]
    total_paths += 1
    if len(countries) > 1 and countries[0] == 'United States' and countries[-1] == 'United States':
        domestic_traffic += 1
        if len(list(set(countries))) > 1:
            total_tromboning += 1
            for c in list(set(countries)):
                if c != 'United States':
                    if c in t_map:
                        t_map[c] += 1
                    else:
                        t_map[c] = 1
    elif len(countries) > 1:
        print countries[-1]

print total_tromboning
print total_paths
for t in t_map:
    print t, t_map[t]
print domestic_traffic
