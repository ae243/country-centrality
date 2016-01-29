import sys
import util

f = open('2015-12-11-13-06-54_domains', 'r')

total_domains = []
for line in f:
	items = line.split(',')
	total_domains.extend(items)
f.close()

final_domains = list(set(total_domains))

clean_domains = list(set(util.clean_targets(final_domains)))

f2 = open('url_check.txt', 'w')
for fd in clean_domains:
	f2.write(fd + ' ' + '\n')
f2.close()
