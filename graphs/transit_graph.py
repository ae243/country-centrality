import sys
import numpy as np
import matplotlib.pyplot as plt

N = 23
menMeans = (1, 2, 3, 4, 5, 6, 6, 8, 10, 19, 24, 35, 50, 96, 284, 427, 773, 952, 1786, 2699, 3089, 6466, 30482)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('# of Paths')
ax.set_title('# of Paths that Solely Transit the Country')
ax.set_xticks(ind + width)
plt.xticks(rotation='vertical')
ax.set_xticklabels(('United Arab Emirates', 'Bahrain', 'Peru', 'Sweden', 'Poland', 'Israel', 'Portugal', 'Uruguay', 'Belgium', 'Colombia', 'China', 'Singapore', 'Japan', 'Venezuela', 'Netherlands', 'Germany', 'Ireland', 'Great Britain', 'France', 'United States', 'Italy', 'Spain', 'Brazil'))
plt.axis([0, 23, 0, 31000])
plt.show()
