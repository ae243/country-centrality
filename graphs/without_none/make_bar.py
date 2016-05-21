import matplotlib.pyplot as plt
import numpy as np
import sys

f = open(sys.argv[1], 'r')
x = []
y = []
num_list = []
num_map = {}
for line in f:
    items = line.split(",")
    num_list.append(int(items[1].strip()))
    if int(items[1].strip()) in num_map:
        num_map[int(items[1].strip())].append(items[0].strip())
    else:
        num_map[int(items[1].strip())] = [items[0].strip()]
f.close()
num_list = list(set(num_list))

sorted_list = sorted(num_list)

for s in sorted_list:
    for s2 in num_map[s]:
        x.append(s2)
        y.append(s)

objects = x
y_pos = np.arange(len(objects))
performance = y
  
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.ylabel('Number of Paths that Contain each Country')

plt.savefig('tex_demo')
plt.show()
