import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import sys

N = 7
avoidance_before = (.896, .919, .969, .992, .994, .994, .997)

ind = np.arange(N)  # the x locations for the groups
width = 0.2       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, avoidance_before, width, color='r')

avoidance_after = (.997, 1.0, .997, 1.0, .997, 1.0, 1.0)
rects2 = ax.bar(ind + width, avoidance_after, width, color='y')

avoidance_bound = (.997, 1.0, .997, 1.0, .997, 1.0, 1.0)
rects3 = ax.bar(ind + width + width, avoidance_bound, width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('Avoidance')
ax.set_xlabel('Country to Avoid')
ax.set_title('Avoidance for Clients in United States')
ax.set_xticks(ind + width + (.5*width))
ax.set_xticklabels(('FR', 'CA', 'NL', 'DE', 'IE', 'GB', 'SG'))

ax.legend((rects1[0], rects2[0], rects3[0]), ('Before', 'After', 'Bound'))

plt.show()
