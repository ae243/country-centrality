import sys

f = open(sys.argv[1], 'r')
for line in f:
    if len(line.split(" ")) > 1 and not 'BR' in line:
        print line
