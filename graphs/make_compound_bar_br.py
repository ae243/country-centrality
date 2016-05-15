import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import sys

N = 8
avoidance_before = (.156, .824, .905, .941, .976, .987, .972, .981)

ind = np.arange(N)  # the x locations for the groups
width = 0.2       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, avoidance_before, width, color='r')

avoidance_after = (.626, 1.0, 1.0, 1.0, 1.0, 1.0, .992, .996)
rects2 = ax.bar(ind + width, avoidance_after, width, color='y')

avoidance_bound = (.886, 1.0, 1.0, 1.0, 1.0, 1.0, .996, .996)
rects3 = ax.bar(ind + width + width, avoidance_bound, width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('Avoidance')
ax.set_xlabel('Country to Avoid')
ax.set_title('Avoidance for Clients in Brazil')
ax.set_xticks(ind + width + (.5*width))
ax.set_xticklabels(('US', 'ES', 'IT', 'FR', 'GB', 'AR', 'IE', 'NL'))

ax.legend((rects1[0], rects2[0], rects3[0]), ('Before', 'After', 'Bound'))

plt.show()
