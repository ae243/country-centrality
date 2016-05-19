import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update(open('matplotlibrc'))


print matplotlib.matplotlib_fname()
f = open(sys.argv[1], 'r')
domain_list = []

for line in f:
    items = line.split(",")[1:-1]
    unique_items = list(set(items))
    domain_list.append(len(unique_items))
f.close()

n, bins, patches = plt.hist(domain_list, 50, facecolor='green')
plt.xlabel('Number of Subsequent Requests')
plt.ylabel('Number of Initial Domain Requests')
plt.axis([0, 200, 0, 60])
#plt.savefig('tex_demo')
plt.show()
