import os, sys,csv, glob
import numpy as np
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from numpy import cumsum

'''
x_us = [0,1,2,3,4,5,6,7,8,9]

y_us = [.46, .59, .63, .66, .66, .66, .66, .66, .66, .66]

y_fr = [.73, .92, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00]

y_de = [.94, .94, .97, .97, .98, .99, .99, .99, .99, .99]

y_uk = [.93, .97, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00]

y_ie = [.82, .94, .96, .96, .96, .97, .97, .97, .97, .97]

y_in = [.98, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00]

fig1, ax1 = plt.subplots(1,1,figsize=(6,5))
plt.plot(x_us,y_us,color='orange',linestyle='-',linewidth=2.0)
plt.plot(x_us,y_ie,color='blue',linestyle=':',linewidth=2.0)
plt.plot(x_us,y_fr,color='red',linestyle='-.',linewidth=2.0)
plt.plot(x_us,y_de,color='green',linestyle=':',linewidth=2.0)
plt.plot(x_us,y_uk,color='purple',linestyle='--',linewidth=2.0)
plt.plot(x_us,y_in,color='pink',linestyle='-.',linewidth=2.0)
#plt.xticks([0,1,2,3], (" ", "DE", "DE,BR", "DE,BR,SG"))
ax1.set_ylabel("Fraction of Domains Accessed while Avoiding a Country",fontsize=14)
ax1.set_xlabel("Number of Relays", fontsize=14)

plt.xticks(np.arange(min(x_us), max(x_us)+1, 1.0))

plt.legend(['United States', 'Ireland', 'France', 'Germany', 'United Kingdom', 'India'], loc='lower right', fontsize=14)

ax1.grid(1)
for tick in ax1.get_yticklabels():
    tick.set_fontsize(14)
for tick in ax1.get_xticklabels():
    tick.set_fontsize(14)
fig1.tight_layout()
ax1.set_xlim([0, 5])
ax1.set_ylim([0, 1.1])
fig1.savefig('avoidance_n_relays.pdf')

'''

#TODO: fix parse_wgets.py
y1 = [2.90689333286,1.27594041628,1.12970225577,0.728782266813,1.44157115653,0.971720356603,0.746985675013,1.00794079526,0.727111689682,0.145590832338,1.05742685049,1.35541354492,1.59316241226,1.25735345748,1.03387540922,1.02593244171,1.10829757121,1.02811823669,1.53146216958,0.809840403473,0.80680582733,0.92796768401,0.522221276954,1.06720252406,6.3930301088,0.928726776012,0.508174866441,1.12129368269,0.651711316354,0.778196669828,1.00729536903,0.889666705219,3.11788340987,1.13986701493,1.30114642621,1.49492693442,0.714679516539,0.907586415423,1.29499480672,0.0626735504715,0.873384556356,0.988450306165,1.00465082914,0.609742201541,0.800802222411,0.951428992655,3.71393035084,2.387075167,0.89811925571,1.09996288383,1.01183690761,0.22760521637,2.18691057968,1.22952194337,1.1547221626,0.905731878652,1.22263710789,1.1880890571,1.40624964789,0.995743690281,1.66796562916,4.56601949807,1.07375657308,1.11333350024,0.704823657074,2.34080041466,0.494530106335,5.15362487519,2.5654834271,0.95331607109,1.09888279102,1.62412090898,0.945324780691,0.758132400492,0.00751652851871,0.419574871325,1.3557812625,1.24778818631,1.11739452947,0.8166095295,0.998229639954,0.63400402393,1.22187009125,4.52947973527,1.20365038712,
2.90689333286,1.27594041628,1.12970225577,0.728782266813,1.44157115653,0.971720356603,0.746985675013,1.00794079526,0.727111689682,0.145590832338,1.05742685049,1.35541354492,1.59316241226,1.25735345748,1.03387540922,1.02593244171,1.10829757121,1.02811823669,1.53146216958,0.809840403473,0.80680582733,0.92796768401,0.522221276954,1.06720252406,6.3930301088,0.928726776012,0.508174866441,1.12129368269,0.651711316354,0.778196669828,1.00729536903,0.889666705219,3.11788340987,1.13986701493,1.30114642621,1.49492693442,0.714679516539,0.907586415423,1.29499480672,0.0626735504715,0.873384556356,0.988450306165,1.00465082914,0.609742201541,0.800802222411,0.951428992655,3.71393035084,2.387075167,0.89811925571,1.09996288383,1.01183690761,0.22760521637,2.18691057968,1.22952194337,1.1547221626,0.905731878652,1.22263710789,1.1880890571,1.40624964789,0.995743690281,1.66796562916,4.56601949807,1.07375657308,1.11333350024,0.704823657074,2.34080041466,0.494530106335,5.15362487519,2.5654834271,0.95331607109,1.09888279102,1.62412090898,0.945324780691,0.758132400492,0.00751652851871,0.419574871325,1.3557812625,1.24778818631,1.11739452947,0.8166095295,0.998229639954,0.63400402393,1.22187009125,4.52947973527,1.20365038712]
x1 = range(1, len(y1)+1)
sorted_y1 = sorted(y1)

fig2, ax2 = plt.subplots(1,1,figsize=(5,3))
'''
plt.plot(x1, sorted_y1, '-', color='orange', linewidth=2.0)
ax2.set_ylabel('Latency Difference (s)', fontsize=14)
ax2.set_xlabel('Top Domains', fontsize=14)

ax2.grid(1)
fig2.tight_layout()
ax2.set_xlim([0,100])
ax2.set_ylim([0,10])
fig2.savefig('latency.pdf')


'''
# the histogram of the data
#n, bins, patches = plt.hist(y1, len(y1), facecolor='orange')
#n = [  1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
#   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,
#   1,   1,   1,   2,   2,   2,   2,   2,   2,   3,   5,   6,  10,  12,  22,
#  67,  75,  77,  79,  79,  79,  80,  80,  80,  81,  81,  81,  81,  81,  81,
#  81,  81,  81,  81,  81,  81,  81,  81,  81,  81,  81,  81,  81,  81,  82,
#  82,  82,  82,  82,  82,  82,  82,  83,]
#new_x = cumsum(n)
#print new_x
#print len(new_x)
#print len(x1)
#plt.plot(n, x1, color='blue', linewidth=2.0)

counts, bin_edges = np.histogram(sorted_y1, bins=100)

# Now find the cdf
cdf = np.cumsum(counts)

print cdf

#print final_cdf
# And finally plot the cdf
plt.plot(bin_edges[1:], cdf)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='minor',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off')

ax2.set_ylabel('Fraction of Domains', fontsize=14)
ax2.set_xlabel('Ratio of RAN throughput to direct throughput (logscale)', fontsize=14)

ylabels = [0,.1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0]
#ax2.set_yticklabels([0,.1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0])
#ax2.set_xticklabels([.01, 1.0, 10.0])
plt.yticks(np.arange(0, 171, 17.0), ylabels)
#plt.yticks(np.arange(0, 1, .1))

ax2.set_xscale("log")
#ax2.grid(1)
fig2.tight_layout()
ax2.set_xlim([0,10])
ax2.set_ylim([0,170])
fig2.savefig('latency.pdf')

