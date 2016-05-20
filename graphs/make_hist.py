import sys
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

f = open(sys.argv[1], 'r')
data = []
for line in f:
    data.append(int(line.strip()))
f.close()

data_map = {}
for d in data:
    if d in data_map:
        data_map[d] += 1
    else:
        data_map[d] = 1

sorted_data = []
inc = 0
for key in sorted(data_map):
    sorted_data.append(int(data_map[key]) + inc)
    inc += int(data_map[key])

print sorted_data

def getCDF(data):
    xdata = np.sort(data)
    ydata = [float(i)/float(len(xdata)) for i in range(len(xdata))]
    return xdata, ydata

fig1, ax1 = plt.subplots(1,1)
xd, yd = getCDF(data)
print xd
print yd
ax1.plot(xd,yd, lw=1)

ax1.set_xlabel("Number of Countries that Host a Domain")
ax1.set_ylabel("Fraction of Domains")
ax1.grid(1)
ax1.legend(loc='best')
fig1.tight_layout()
#format_axes(ax1)

#n, bins, patches = plt.hist(data, 21, facecolor='green')

#plt.xlabel('Number of Different Countries that Host a Domain')
#plt.ylabel('Number of Domains')
#plt.title('Histogram of Unique Countries that Host Domains')
plt.savefig('tex_demo')
plt.show()
