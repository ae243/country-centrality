import sys
import numpy as np
import matplotlib.pyplot as plt

N = 9
menMeans = (8, 12, 12, 20, 20, 24, 177, 251, 1248)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('# of Paths')
ax.set_title('# of Paths that Trombone from Brazil')
ax.set_xticks(ind + width)
plt.xticks(rotation='vertical')
ax.set_xticklabels(('China', 'Colombia', 'Germany', 'France', 'Ireland', 'Great Britain', 'Italy', 'Spain', 'United States'))
plt.axis([0, 9, 0, 1300])
plt.show()
