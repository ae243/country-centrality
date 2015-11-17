import sys

f = open(sys.argv[1], 'r')
prev_rtt = ''
for line in f:
	if line[0] == '1':
		# no rtt comparison
		rtt = line.split(' ')[2]
		prev_rtt = rtt
	elif not line[0] == '#':
		# compare rtt
		rtt = line.split(' ')[2]
		prev_rtt = rtt
		# if rtt comparison doesn't resolve it, then do nslookup to get router name
		# if reverse dns lookup doesn't work, then query whois or MaxMind
		# if none of the above gives a good conclusion for an IP address, then return that address and we can run a traceroute to it using RIPE atlas
f.close()
