import sys

f = open('domains.txt', 'r')
domains = []
for line in f:
    domains.append(line.strip())
f.close()

file_list = ['cc_brazil.txt', 'cc_brazil-vps.txt', 'cc_oregon.txt', 'cc_ireland.txt', 'cc_frankfurt.txt', 'cc_tokyo.txt', 'cc_seoul.txt', 'cc_singapore.txt', 'cc_singapore-vps.txt', 'cc_sydney.txt', 'cc_france.txt', 'cc_spain.txt']

found = []
for filename in file_list:
    f = open(filename, 'r')
    f2 = open('filter_' + filename, 'w')
    for line in f:
        if line.split("|")[0] in domains:
            f2.write(line)
            found.append(line.split("|")[0].strip())
    f.close()
    f2.close()

found = set(found)

not_found = set(domains).difference(found)
print len(not_found)
print not_found
