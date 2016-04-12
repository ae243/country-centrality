import sys

cc = sys.argv[1]

cc_count = 0
count = 0
f = open('country_paths.txt', 'r')
for line in f:
    items = line.split(" ")
    items = list(set(items))
    if len(items) > 0:
        if cc in items:
            cc_count += 1
        count += 1

print cc_count
print count

fraction = float(cc_count)/float(count)

print str( 1 - fraction)
