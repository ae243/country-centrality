import sys

# MaxMind Dataset <ip, Country>
f1 = open(sys.argv[1], 'r')
mm_map = {}
for line in f1:
    if len(line.strip().split(",")) > 1:
        ip = line.split(",")[0]
        country = line.split(",")[1]
        mm_map[ip] = country
    else:
        ip = line.split(" ")[0]
        country = 'None'
        mm_map[ip] = country
f1.close()

n_count1 = 0
for x in mm_map:
    if mm_map[x] == 'None':
        print x
        n_count1 += 1
print "MaxMind 'None' count = " + str(n_count1)

c_map = {'usa': "United States", 'jpn': "Japan", 'zaf': "South Africa", 'twn': "Taiwan", 'deu': "Germany", 'mex': "Mexico", 'prt': "Portugal", 'gbr': "United Kingdom", 'nld': "Netherlands", 'ven': "Venezuela", 'rus': "Russia", 'hkg': "Hong Kong", 'bra': "Brazil", 'can': "Canada", 'None': 'None'}

# Digital Envoy Dataset <ip, cc>
f2 = open(sys.argv[2], 'r')
de_map = {}
for line in f2:
    if len(line.split(" ")) > 2:
        ip = line.split(":")[0]
        cc = c_map[line.split(",")[2][2:-1]]
        de_map[ip] = cc
    else:
        ip = line.split(":")[0]
        cc = 'None'
        de_map[ip] = cc
f2.close()

n_count2 = 0
for x in de_map:
    if de_map[x] == 'None':
        n_count2 += 1
print "DE 'None' count = " + str(n_count2)

count = 0
for ip in mm_map:
    if mm_map[ip] != de_map[ip]:
        count += 1
        print mm_map[ip], de_map[ip], ip
