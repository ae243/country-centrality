import util
import sys

domains = []
f = open('brazil_domains.txt', 'r')
for line in f:
    domains.append(line.strip())
f.close()

dns_measurement_ids = util.run_DNS_measurements(domains)
print "DNS MEASURMENT IDS:"
print dns_measurement_ids
print "\n"

time.sleep(600) # wait for 20 minutes for DNS measurements to end - is there a better way to do this?
ips = util.analyze_DNS_measurements(dns_measurement_ids)

for ip in ips:
    # geolocate the ip using maxmind
