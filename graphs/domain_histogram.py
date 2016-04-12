import sys
import matplotlib.pyplot as plt

f = open(sys.argv[1], 'r')
domain_list = []

for line in f:
    items = line.split(",")[1:-1]
    unique_items = list(set(items))
    domain_list.append(len(unique_items))
f.close()

n, bins, patches = plt.hist(domain_list, 50, facecolor='green')
plt.xlabel('# of Subsequent Requests')
plt.ylabel('# of Initial Domain Requests')
plt.title('Histogram of Subsequent Requests made for Initial Domain Request')
plt.axis([0, 200, 0, 60])
plt.show()
