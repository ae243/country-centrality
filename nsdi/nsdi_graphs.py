import os, sys,csv, glob
import numpy as np
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt

x = [0,1,2,3]
y = [.2, .6, .8, .85]

fig1, ax1 = plt.subplots(1,1,figsize=(5,6))
plt.plot(x,y,color='orange',linewidth=2.0)
plt.xticks([0,1,2,3], (" ", "DE", "DE,BR", "DE,BR,SG"))
ax1.set_ylabel("Fraction of domains accessed without traversing Country X",fontsize=14)
ax1.set_xlabel("Set of Relays", fontsize=14)

ax1.grid(1)
for tick in ax1.get_yticklabels():
    tick.set_fontsize(14)
for tick in ax1.get_xticklabels():
    tick.set_fontsize(14)
fig1.tight_layout()
ax1.set_xlim([0, 3])
ax1.set_ylim([0, 1])
fig1.savefig('avoidance_n_relays.pdf')

x1 = range(1, 101)
y1 = []

x2 = x1
y2 = []

fig2, ax2 = plt.subplots(1,1,figsize=(5,6))
plt.plot(x1, y1, 'r--', x2, y2, 'bs')
ax2.set_ylabel('Latency (ms)', fontsize=14)
ax2.set_xlabel('Top 100 Domains', fontsize=14)

ax2.grid(1)
fig2.tight_layout()
ax2.set_xlim([0,100])
ax2.set_ylim([0,50])
fig2.savefig('latency.pdf')
