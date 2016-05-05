import sys

total_tromboning = 0
total_paths = 0
t_map = {}
d_map = {} # <domain, is_tromboning>
f_list = [sys.argv[1], sys.argv[2]]
for f in f_list:
    f = open(f, 'r')
    for line in f:
        items = line.strip().split("|")
        domain = items[0]
        countries = items[1:]
        total_paths += 1
        if domain in d_map and d_map[domain] == False:
            continue
        else:
            if len(countries) > 1 and countries[0] == 'Brazil' and countries[-1] == 'Brazil':
                if list(set(countries)) > 1:
                    total_tromboning += 1
                    d_map[domain] = True
                    for c in list(set(countries)):
                        if c != 'Brazil':
                            if c in t_map:
                                t_map[c] += 1
                            else:
                                t_map[c] = 1
                else:
                    d_map[domain] == False
    f.close()

print total_tromboning
print total_paths
for t in t_map:
    print t, t_map[t]
