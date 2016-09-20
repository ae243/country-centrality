import os, sys,csv, glob
import numpy as np
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from numpy import cumsum

# Country Avoidance Plot
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

# Throughput Plot

y1 = [0.934000232861,0.456565046957,1.18241484604,0.234671336942,0.670741925359,1.08775324039,0.0423117459887,0.0298067224663,1.17368824443,0.0061533631901,
1.41235794537,0.7728701116,1.89613862729,1.4341991286,0.592081758454,1.20360644454,0.827148864896,1.03601373535,1.57018712121,1.01881287805,0.361025649927,
2.23095587412,0.994877154324,0.946063405724,0.962810540827,0.0477562317971,0.987269488258,0.731464820517,39.1537351403,1.55619569527,0.434022562541,1.06213600525,
0.606440775712,0.0844545804136,1.19843146532,0.960488961452,1.44195932283,0.485439294414,0.940023927896,1.0348347236,0.130064275507,1.0037299124,0.671530049828,
0.357746327689,0.694466126241,0.709674680424,0.584421705432,0.871573196542,0.546981748971,1.5105814454,0.0153834245679,0.274198413439,1.20734016122,0.955694668242,
0.778061506852,0.378226429292,0.827265175106,1.21970098755,0.461815440209,0.493828398207,0.724056395226,2.85763944255,1.27728788091,1.29612587475,0.854892201166,
1.13306926926,1.12934653022,0.865267312671,1.0319199371,0.944779931621,0.0839459398283,0.271992608676,0.44686586338,0.136126120069,0.620091604777,0.824879547226,
0.855493344235,0.295660225241,0.943048577208,0.203620295552,0.916193090628,1.00599645757,0.995336346737,0.00988249770003,0.921362830409,1.85390576056,1.21090563989,
1.39003052836,0.666859699714,1.01785037258,1.0535152694,0.612032688678,0.952224939079,0.462040084292,1.01398741727]
x1 = range(1, len(y1)+1)
sorted_y1 = sorted(y1)

print sorted_y1

fig2, ax2 = plt.subplots(1,1,figsize=(5,3))

counts, bin_edges = np.histogram(sorted_y1, bins=1000)

# Now find the cdf
cdf = np.cumsum(counts)

# And finally plot the cdf
plt.plot(bin_edges[1:], cdf)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='minor',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off')

ax2.set_ylabel('Fraction of Domains', fontsize=14)
ax2.set_xlabel('Ratio of direct throughput to RAN throughput (logscale)', fontsize=14)

ylabels = [0,.1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0]
plt.yticks(np.arange(0, 96, 9.5), ylabels)

ax2.set_xscale("log")
ax2.grid(1)
fig2.tight_layout()
ax2.set_xlim([0,10])
ax2.set_ylim([0,95])
fig2.savefig('throughput.pdf')


'''
# Latency Plot
y1 = [0.09059999999999999, 0.155, 0.0732, 0.05639999999999999, 0.0779, 0.0683, 0.0774, 0.35900000000000004, 0.4955, 0.1817, 0.542, 0.08589999999999998, 0.053099999999999994, 0.10269999999999999, 0.1265, 0.3435, 0.2947, 0.05519999999999999, 0.06259999999999999, 0.4655, 0.0517, 0.2185, 0.0632, 0.1575, 0.09519999999999999, 0.0462, 0.4034999999999999, 0.1446, 0.19140000000000001, 0.0521, 0.10699999999999998, 0.20270000000000002, 0.3782, 0.46299999999999997, 0.04439999999999999, 0.06899999999999999, 0.07129999999999999, 0.1835, 0.0353, 0.04599999999999999, 0.1737, 0.0819, 0.2617, 0.0699, 0.1934, 0.05319999999999999, 0.1756, 0.5641, 0.0675, 0.16319999999999998, 0.0739, 0.05650000000000001, 0.045899999999999996, 0.15819999999999998, 0.16060000000000002, 0.057600000000000005, 0.06410000000000002, 0.12249999999999998, 0.06999999999999999, 0.4074, 0.055499999999999994, 0.17909999999999998, 0.06359999999999999, 14.241600000000002, 0.0377, 0.05419999999999999, 0.0364, 0.27690000000000003, 0.09730000000000001, 0.05289999999999999, 0.08979999999999999, 0.10189999999999999, 0.09209999999999999, 0.4190999999999999, 0.25420000000000004, 0.24410000000000004, 0.13130000000000003, 0.1199, 0.1575, 0.0505, 0.1045, 0.14900000000000002, 0.0673, 0.1722, 0.129, 0.03679999999999999, 0.3454, 0.09669999999999998, 0.1091, 0.4037, 0.07990000000000003, 0.1255, 0.0629, 0.054700000000000006, 0.0759, 0.08889999999999998, 1.9205999999999999, 0.0626, 0.2829, 0.0996]

y2 = [0.061, 0.13, 0.106, 0.044, 0.047, 0.055, 0.063, 0.116, 0.417, 0.039, 0.03, 0.062, 0.053, 0.078, 0.125, 0.293, 0.189, 0.036, 0.048, 0.417, 0.064, 0.205, 0.038, 0.052, 0.076, 0.031, 0.0, 0.074, 0.142, 0.036, 0.099, 0.069, 0.199, 0.51, 0.038, 0.058, 0.057, 0.046, 0.023, 0.045, 0.136, 0.037, 0.269, 0.024, 0.225, 0.037, 0.098, 0.198, 0.073, 0.054, 0.088, 0.053, 0.027, 0.136, 0.043, 0.035, 0.066, 0.032, 0.068, 0.05, 0.088, 0.138, 0.048, 0.0, 0.024, 0.026, 0.023, 0.107, 0.07, 0.031, 0.028, 0.345, 0.076, 0.228, 0.1, 0.066, 0.1, 0.173, 0.195, 0.038, 0.076, 0.13, 0.093, 0.074, 0.086, 0.024, 0.305, 0.09, 0.086, 0.508, 0.104, 0.05, 0.053, 0.067, 0.073, 0.07, 1.756, 0.058, 0.067, 0.087]

x1 = range(1,len(y1)+1)
sorted_y1 = sorted(y1)
sorted_y2 = sorted(y2)

print np.percentile(sorted_y1, 50)
print np.percentile(sorted_y1, 90)

print np.percentile(sorted_y2, 50)
print np.percentile(sorted_y2, 90)

fig3, ax3 = plt.subplots(1,1,figsize=(5,3))

counts, bin_edges = np.histogram(sorted_y1, bins=1000)
counts2, bin_edges2 = np.histogram(sorted_y2, bins=1000)

cdf = np.cumsum(counts)
cdf2 = np.cumsum(counts2)

plt.plot(bin_edges[1:], cdf, linestyle='-', linewidth=2.0)
plt.plot(bin_edges2[1:], cdf2, linestyle='--',linewidth=2.0)

plt.legend(['With RAN', 'Direct'], loc='lower right', fontsize=14)

ax3.set_ylabel('Fraction of Domains',fontsize=14)
ax3.set_xlabel('Time to First Byte (s)',fontsize=14)

ylabels = [0,.1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0]
plt.yticks(np.arange(0, 101, 10.0), ylabels)

fig3.tight_layout()
ax3.set_xlim([0.0, 1.0])
ax3.set_ylim([0.0,100])
fig3.savefig('latency.pdf')
'''
