import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import sys

f = open(sys.argv[1], 'r')
x = []
y = []
for line in f:
    items = line.split(" ")
    x.append(items[0].strip())
    y.append(int(items[1].strip()))
f.close()

objects = x
y_pos = np.arange(len(objects))
performance = y
  
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.ylabel('Number of Paths that Contain each Country')
#plt.title('Countries that Transit Tromboning ' + sys.argv[2] + '  Traffic')

''' 
This will put a label on top of the bar - put the number of unique IP addresses that geolocate to the country there.
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
'''
plt.savefig('tex_demo')   
plt.show()
