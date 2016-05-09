import sys
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

f = open(sys.argv[1], 'r')
data = []
for line in f:
    data.append(int(line.strip()))
f.close()

n, bins, patches = plt.hist(data, 21, facecolor='green')

plt.xlabel('# of Different Countries that Host a Domain')
plt.ylabel('# of Domains')
plt.title('Histogram of Unique Countries that Host Domains')
plt.show()
