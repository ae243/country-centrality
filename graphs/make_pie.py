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
    if count == 0:
        total_paths = int(line.strip())
    elif len(line.strip().split(" ")) == 1:
        current_country = line.strip()
    elif line.split(":")[0] == 'Hosted':
        c_host[current_country] = float(line.split(" ")[1].strip())/float(total_paths)
    elif line.split(":")[0] == 'Transits':
        c_transit[current_country] = float(line.split(" ")[1].strip())/float(total_paths)
    count += 1
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

plt.title('Countries that Host ' + sys.argv[2] + ' Traffic', bbox={'facecolor':'0.8', 'pad':5})
plt.show()
