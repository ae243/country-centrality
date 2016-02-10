import sys
import numpy as np
import matplotlib.pyplot as plt

N = 31
menMeans = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 4, 7, 7, 10, 18, 30, 37, 37, 38, 39, 61, 68, 111, 435, 560, 643, 6351, 28196)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('Countries')
ax.set_title('# of Paths that End in the Country')
ax.set_xticks(ind + width)
plt.xticks(rotation='vertical')
ax.set_xticklabels(('Belgium', 'China', 'Colombia', 'Great Britain', 'Peru', 'Poland', 'Portugal', 'Singapore', 'United Arab Emirates', 'Venezuela', 'Bahrain', 'Uruguay', 'Chile', 'Israel', 'France', 'Sweden', 'Japan', 'Spain', 'Italy', 'British Virgin Islands', 'Canada', 'Ukraine', 'Czech Republic', 'Costa Rica', 'Germany', 'Guatemala', 'Netherlands', 'Argentina', 'Ireland', 'Brazil', 'United States'))
plt.axis([0, 31, 0, 29000])
plt.show()
