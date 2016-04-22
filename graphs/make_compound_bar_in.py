import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import sys

N = 8
avoidance_before = (.285, .796, .731, .896, .954, .879, .969, .988)

ind = np.arange(N)  # the x locations for the groups
width = 0.2       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, avoidance_before, width, color='r')

avoidance_after = (.667, 1.0, .95, 1.0, 1.0, .997, .994, .997)
rects2 = ax.bar(ind + width, avoidance_after, width, color='y')

avoidance_bound = (.778, 1.0, .953, 1.0, 1.0, .997, 1.0, .997)
rects3 = ax.bar(ind + width + width, avoidance_bound, width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('Avoidance')
ax.set_xlabel('Country to Avoid')
ax.set_title('Avoidance for Clients in India')
ax.set_xticks(ind + width + (.5*width))
ax.set_xticklabels(('US', 'GB', 'SG', 'FR', 'AU', 'NL', 'IE', 'PL'))

ax.legend((rects1[0], rects2[0], rects3[0]), ('Before', 'After', 'Bound'))

plt.show()
