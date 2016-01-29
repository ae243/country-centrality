import sys

f = open(sys.argv[1], 'r')
count = 0
for line in f:
    items = line.split(':')
    if items[0] == '1':
        count += 1
#    if line.strip() == '255: ***':
#        count += 1
print count
