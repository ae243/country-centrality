import sys

f = open(sys.argv[1], 'r')
totals = 0.00
denom = 0.00
mult = 0.00
for line in f:
    totals += float(line.strip())
    denom += 1.00
    if float(line.strip()) > 1.00:
        mult += 1.00
f.close()

print totals/denom

print mult/denom
