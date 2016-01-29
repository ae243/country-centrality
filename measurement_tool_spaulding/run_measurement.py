#!/usr/bin/python

# this script gathers measurements using the following methodology:
#   1) curl the list of domains in domains.txt
#   2) extract urls from the domain's web page
#   3) run DNS measurements for all domains in the web page, as well as the original domain
#   4) run traceroute measurements for all DNS responses (from corresponding probes)
#   5) map traceroutes to country-level paths
#   6) store traceroutes and country-level paths in some sort of structure/database/location
# We use the RIPE Atlas API to create measurements, which can be found here: https://atlas.ripe.net/docs/measurement-creation-api/
# We use the RIPE Atlas API to fetch measurements, which looks like: https://atlas.ripe.net/api/v1/measurement/<measurementID>/result/

# usage: python run_measurement.py 

import sys
import util
import time
import datetime

fmt = "%Y-%m-%d-%H-%M-%S"
date_time_stamp = datetime.datetime.now().strftime(fmt)
f = open(date_time_stamp + '_log.txt', 'w')
f.close()

ts1 = time.time()
time_start = datetime.datetime.fromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S')
targets = []
total_urls = []
#domains_file = open('domains.txt', 'r')
#for domain in domains_file:
#    
    # 1) curl the list of domains in domains.txt -- currently uses planetlab
#    page = util.curl(domain.strip())
    
    # 2) extract the urls from the domains's web page
#    urls = [domain]
#    urls.extend(util.extract_urls(page))
#    total_urls.append(urls)
#    targets.extend(urls)

# 3) store domains and urls
#util.store_domains(total_urls)
#domains_file.close()

# THIS IS TEMPORARY WHILE THERE IS NO PLANETLAB SLICE *********

f_all_domains = open('domains_subdomains.txt', 'r')
for line in f_all_domains:
    items = line.split(',')
    targets.extend(items)
f_all_domains.close()

# *************************************************************

# 4) Modify targets to include 'correct' urls
targets = list(set(util.clean_targets(targets)))

if '' in targets:
    targets.remove('')

f_log = open(date_time_stamp + '_log.txt', 'a')
f_log.write('Targets: ' + str(targets) + '\n')
f_log.close()
print "TARGETS:"
print targets
print "\n"

# 4) run DNS measurements for all domains in the web page, as well as the original domain
dns_measurement_ids = util.run_DNS_measurements(targets)

f_log = open(date_time_stamp + '_log.txt', 'a')
f_log.write('DNS Measurement IDs: ' + str(dns_measurement_ids) + '\n')
f_log.close()
print "DNS MEASURMENT IDS:"
print dns_measurement_ids
print "\n"

time.sleep(600) # wait for 20 minutes for DNS measurements to end - is there a better way to do this?
ips = util.analyze_DNS_measurements(dns_measurement_ids)

f_log = open(date_time_stamp + '_log.txt', 'a')
f_log.write('IP Address Targets: ' + str(ips) + '\n')
f_log.close()
print "IP ADDRESSES:"
print ips
print "\n"

# get one ip address per /24
ips = util.consolidate_ips(ips)

# 5) run traceroute measurements for all DNS responses (from corresponding probes)
traceroute_measurement_ids = util.run_traceroute_measurements(ips, 'ICMP')
traceroute_measurement_ids.extend(util.run_traceroute_measurements(ips, 'TCP'))

f_log = open(date_time_stamp + '_log.txt', 'a')
f_log.write('Traceroute Measurement IDs: ' + str(traceroute_measurement_ids) + '\n')
f_log.close()
print "TRACE MEASUREMENT IDS:"
print traceroute_measurement_ids
print "\n"

time.sleep(600) # wait for 30 minutes for traceroute measurements to end - is there a better way to do this?
traceroutes = util.analyze_traceroute_measurements(traceroute_measurement_ids)

print "TRACEROUTES:"
print traceroutes
print "\n"

# 6) store traceroutes and domains (with urls)
util.store_traces(traceroutes)

ts2 = time.time()
time_end = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')

f_log = open(date_time_stamp + '_log.txt', 'a')
f_log.write('Time start: ' + str(time_start) + '\n')
f_log.write('Time end: ' + str(time_end) + '\n')
f_log.close()
