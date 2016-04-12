import sys
import util

ids = ['3672011', '3672012', '3672013', '3672014', '3672015', '3672016', '3672017', '3672018', '3672019', '3672020', '3672021', '3672022']

traces = util.analyze_traceroute_measurements(ids)

f = open(sys.argv[1], 'w')
for t in traces:
    for t2 in t:
        items = t2.split(": ")
        hop = items[0].strip()
        ip = items[1].split(" ")[0].strip()
        f.write(hop + " (" + ip + ") \n")
f.close()
