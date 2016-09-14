import os, sys,csv, glob
import numpy as np
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from numpy import cumsum


x_us = [0,1,2,3,4,5,6,7,8,9]

y_us = [.46, .59, .63, .66, .66, .66, .66, .66, .66, .66]

y_fr = [.73, .92, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00]

y_de = [.94, .94, .97, .97, .98, .99, .99, .99, .99, .99]

y_uk = [.93, .97, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00]

y_ie = [.82, .94, .96, .96, .96, .97, .97, .97, .97, .97]

y_in = [.98, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00]

fig1, ax1 = plt.subplots(1,1,figsize=(6,5))
plt.plot(x_us,y_us,color='orange',linewidth=2.0)
plt.plot(x_us,y_ie,color='blue',linewidth=2.0)
plt.plot(x_us,y_fr,color='red',linewidth=2.0)
plt.plot(x_us,y_de,color='green',linewidth=2.0)
plt.plot(x_us,y_uk,color='purple',linewidth=2.0)
plt.plot(x_us,y_in,color='pink',linewidth=2.0)
#plt.xticks([0,1,2,3], (" ", "DE", "DE,BR", "DE,BR,SG"))
ax1.set_ylabel("Fraction of Domains Accessed while Avoiding a Country",fontsize=14)
ax1.set_xlabel("Number of Relays", fontsize=14)

plt.xticks(np.arange(min(x_us), max(x_us)+1, 1.0))

plt.legend(['United States', 'Ireland', 'France', 'Germany', 'United Kingdom', 'India'], loc='lower right')

ax1.grid(1)
for tick in ax1.get_yticklabels():
    tick.set_fontsize(14)
for tick in ax1.get_xticklabels():
    tick.set_fontsize(14)
fig1.tight_layout()
ax1.set_xlim([0, 9])
ax1.set_ylim([0, 1.1])
fig1.savefig('avoidance_n_relays.pdf')

'''

#TODO: fix parse_wgets.py
y1 = [-0.07345108642831227, 0.0007663840851891424, -.0000068850951969662625, 0.017090706709771045, .00009037723008089487, -0.03739333800151113, -.000048860644443178905, -0.0001156129061229646, 0.0015405375733514564, 0.0007615865202302563, -0.0012956761874072, 0.09637029029727928, 0.4298142668579807, -0.03546828721698962, -0.007669176518082799, -0.05725748434975764, 0.0012947884259059458, -.0000615767940439966, -0.0035141077799943805, 0.015764012877323555, 0.02668775511028045, -.00001865780438122487, 0.03910762051121945, 0.013949122333133532, 0.0003958033702267823, 0.002354460356575499, -0.004377101904512959, -0.0009284004508941387, -0.013099607920699946, -.0000715039243327515, -0.0009227417327545501, 0.14189131041519787, 0.004071950165081921, -.0000875958908716501, 0.05531670332793653, 0.004307831811006888, -0.0017661209345716461, -0.07950183895661941, .000005456646592518795, 0.5550528512106119, 0.0008359283191335665, 0.022131392549862502, 0.01336809691665716, .00006777193188321708, 0.023187741212379237, 0.0023022191277865707, -.00002044501820007728, -0.0024255418522472682, 0.04640812981579624, -0.06026106901069267, -0.6601279314263597, 0.0011077999943925124, 0.0003371541775622905, .00000019958381415757323, -0.03648370118785888, -0.0017628864747803417, 0.012668541499546595, -0.007395347994435971, .0000020438002788608694, 0.015592259450983019, -0.00013593988355108458, 0.006523116224314703, -0.02269755115009954, 0.0027934836733872724, -.000012219442354615909, -.0000007212554305457252, 0.0004039780244794824, -0.020080927013193736, -.00002688219696721949, .000013669936224837138, -0.000773993505157044, 0.0002151040279616055, -0.03608043421760443, -0.012533008582476461, 0.0005350295125020003, -0.16655071916937353, 0.0002358402693212647, 0.0002166178018501851, 0.029149303699974132, 0.0027290324461624917, 0.006959415937253568, -.00003456306835543203, 0.00010418950932476745]
x1 = range(1, 84)
sorted_y1 = sorted(y1)

fig2, ax2 = plt.subplots(1,1,figsize=(5,5))

plt.plot(x1, sorted_y1, 'o', color='orange', linewidth=2.0)
ax2.set_ylabel('Latency Difference (s)', fontsize=14)
ax2.set_xlabel('Top Domains', fontsize=14)

ax2.grid(1)
fig2.tight_layout()
ax2.set_xlim([0,100])
ax2.set_ylim([-.7,.7])
fig2.savefig('latency.pdf')
'''

'''
# the histogram of the data
n, bins, patches = plt.hist(y1, 83, facecolor='orange')
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

ax2.set_ylabel('Frequency', fontsize=14)
ax2.set_xlabel('Latency Difference (s)', fontsize=14)

ax2.grid(1)
fig2.tight_layout()
ax2.set_xlim([-.7,.7])
ax2.set_ylim([0,60])
fig2.savefig('latency.pdf')

'''
