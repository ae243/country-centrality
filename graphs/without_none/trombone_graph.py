import sys
import numpy as np
import matplotlib.pyplot as plt

N = 10
menMeans = (8, 13, 35, 36, 49, 71, 82, 140, 1073, 1340)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('# of Paths')
ax.set_title('# of Paths that Trombone from the United States')
ax.set_xticks(ind + width)
plt.xticks(rotation='vertical')
ax.set_xticklabels(('India', 'Hong Kong', 'Great Britain', 'Singapore', 'Germany', 'Ireland', 'Netherlands', 'Canada', 'France', 'None'))
plt.axis([0, 10, 0, 1400])
plt.show()
