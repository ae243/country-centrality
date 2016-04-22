import sys

f = open('cc_paths.txt', 'r')
path_map1 = {} # <(from,to), [list of countries on path]>
path_map2 = {}
for line in f:
    items = line.strip().split("|")
    fro = items[0]
    to = items[1]
    countries = items[2:]
    if fro != '' and to != '':
        if (to,fro) in path_map1:
            path_map2[(fro,to)] = countries
        else:
            path_map1[(fro,to)] = countries
f.close()

cleaned_paths1 = {}
# clean up pairs
for p in path_map1:
    fro = p[0]
    to = p[1]
    if (to,fro) in path_map2:
        cleaned_paths1[p] = path_map1[p]

exact_list = 0
same_set = 0
is_subset = 0
total = 0
for p in cleaned_paths1:
    fro = p[0]
    to = p[1]
    countries = cleaned_paths1[p]
    for p2 in path_map2:
        if p2 == (to, fro):
            countries2 = path_map2[p2]
            # compare countries to reverse(countries2)
            c2 = list(reversed(countries2))
            c2 = [value for value in c2 if value != 'None']
            c1 = [value for value in countries if value != 'None']
            if c1 == c2:
                exact_list += 1
            if set(c1) == set(c2):
                same_set += 1
            if set(c2) <= set(c1):
                is_subset += 1
#            if c1 != c2 and set(c1) != set(c2) and set(c2) > set(c1):
#                print fro,to
#                print set(c1)
#                print set(c2)


print "Exact country path comparison success: " + str(exact_list)
print "Same country set comparison success: " + str(same_set)
print "Reverse set is a subset of the forward set success: " + str(is_subset)
print "Number of path pairs: " + str(len(cleaned_paths1))
