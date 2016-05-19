import sys
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

f = open(sys.argv[1], 'r')
domain_list = []

for line in f:
    items = line.split(",")[1:-1]
    unique_items = list(set(items))
    domain_list.append(len(unique_items))
f.close()

#n, bins, patches = plt.hist(domain_list, 50, facecolor='green')
d_map = {}
for d in domain_list:
    if d in d_map:
        d_map[d] += 1
    else:
        d_map[d] = 1

keylist = d_map.keys()
keylist.sort()
final_map = {}
for key in keylist:
    final_map[key] = d_map[key]

x = len(final_map)
cy = np.cumsum(d_map.values())
plt.plot(x,cy)
plt.show()
#plt.xlabel('# of Subsequent Requests')
#plt.ylabel('# of Initial Domain Requests')
#plt.title('Histogram of Subsequent Requests made for Initial Domain Request')
#plt.axis([0, 200, 0, 60])
#plt.show()
