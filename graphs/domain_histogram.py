import sys
import matplotlib.pyplot as plt

f = open(sys.argv[1], 'r')
domain_list = []

for line in f:
    x = line.strip()
    domain_list.append(x)
f.close()

n, bins, patches = plt.hist(domain_list, 50, facecolor='green')
plt.xlabel('Number of Subsequent Requests')
plt.ylabel('Number of Initial Domain Requests')
plt.axis([0, 200, 0, 60])
#plt.savefig('tex_demo')
plt.show()
