import sys
import util

traceroute_measurement_ids = ['3078061']

traceroutes = util.analyze_traceroute_measurements(traceroute_measurement_ids)

print "TRACEROUTES:"
print traceroutes
print "\n"
