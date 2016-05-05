import sys
import matplotlib.pyplot as plt
import operator

fig = plt.figure(figsize=[10, 9])
ax = fig.add_subplot(111)

f = open(sys.argv[1], 'r')
count = 0
total_paths = 0
current_country = ''
c_host = {}
c_transit = {}
for line in f:
    current_country = line.split(",")[0].strip()
    frac = line.split(",")[3].strip()
    c_host[current_country] = frac
f.close()

sorted_x = sorted(c_host.items(), key=operator.itemgetter(1))
sorted_x.reverse()

labels = []
fracs = []
for t in sorted_x:
    labels.append(t[0])
    fracs.append(t[1])

explode = [.05] * len(sorted_x)

patches, text = plt.pie(fracs, explode=explode, labels=labels, labeldistance=1.05)

plt.title('Countries that Host ' + sys.argv[2] + ' Traffic (Top 100 Domains)', bbox={'facecolor':'0.8', 'pad':5})
plt.show()
