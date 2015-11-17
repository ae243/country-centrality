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

f = open('log.txt', 'w')
f.close()

for domain in open('domains.txt', 'r'):
    # 1) curl the list of domains in domains.txt -- currently uses planetlab
    # TODO: have RIPE Atlas send the HTTP or HTTPS request
    page = util.curl(domain.strip())
    if page == "":
        # this is an error on curling the domain
        continue

    # 2) extract the urls from the domains's web page
#    urls = util.extract_urls(page)
#    urls.append(domain.strip())

    # 3) run DNS measurements for all domains in the web page, as well as the original domain
#    ips = util.run_DNS_measurements(urls)
    ips = []
    # 4) run traceroute measurements for all DNS responses (from corresponding probes)
#    traceroutes = util.run_traceroute_measurements(ips)

    # 5) map traceroutes to country-level paths
#    country_paths = util.get_country_level_paths(traceroutes)

    # 6) store traceroutes and country-level paths in some sort of structure/database/location
#    util.store(traceroutes)
#    util.store(country_paths)
