import sys

f = open(sys.argv[1], 'r')
count = 1
domain_count = 0
for line in f:
	if count == 50:
		print domain_count
	domain_count += len(line.split(','))
	count += 1
