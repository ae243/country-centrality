# this script gathers measurements using the following methodology:
#   1) curl the list of domains in domains.txt
#   2) extract urls from the domain's web page
#   3) run DNS measurements for all domains in the web page, as well as the original domain
#   4) run traceroute measurements for all DNS responses (from corresponding probes)
#   5) map traceroutes to country-level paths
#   6) store traceroutes and country-level paths in some sort of structure/database/location
# NOTE: you must be logged into RIPE Atlas for this script to run successfully.
# We use the RIPE Atlas API to create measurements, which can be found here: https://atlas.ripe.net/docs/measurement-creation-api/
# We use the RIPE Atlas API to fetch measurements, which looks like: https://atlas.ripe.net/api/v1/measurement/<measurementID>/result/

# usage: python run_measurement.py 

import sys
import util
import time

f = open('log.txt', 'w')
f.close()

targets = []
total_urls = []
domains_file = open('domains.txt', 'r')
for domain in domains_file:
    
    # 1) curl the list of domains in domains.txt -- currently uses planetlab
    page = util.curl(domain.strip())
    
    # 2) extract the urls from the domains's web page
    urls = [domain]
    urls.extend(util.extract_urls(page))
    total_urls.append(urls)
    targets.extend(urls)

# 3) store domains and urls
util.store_domains(total_urls)
domains_file.close()

# 4) Modify targets to include 'correct' urls
targets = util.clean_targets(targets)

print "TARGETS:"
print targets
print "\n"

# 4) run DNS measurements for all domains in the web page, as well as the original domain
dns_measurement_ids = util.run_DNS_measurements(targets)
print "DNS MEASURMENT IDS:"
print dns_measurement_ids
print "\n"

time.sleep(600) # wait for 20 minutes for DNS measurements to end - is there a better way to do this?
ips = util.analyze_DNS_measurements(dns_measurement_ids)

print "IP ADDRESSES:"
print ips
print "\n"

# 5) run traceroute measurements for all DNS responses (from corresponding probes)
traceroute_measurement_ids = util.run_traceroute_measurements(ips, 'ICMP')
traceroute_measurement_ids.extend(util.run_traceroute_measurements(ips, 'TCP'))
time.sleep(600) # wait for 30 minutes for traceroute measurements to end - is there a better way to do this?
traceroutes = util.analyze_traceroute_measurements(traceroute_measurement_ids)

print "TRACE MEASUREMENT IDS:"
print traceroute_measurement_ids
print "\n"

print "TRACEROUTES:"
print traceroutes
print "\n"

# 6) store traceroutes and domains (with urls)
util.store_traces(traceroutes, sys.argv[1])
