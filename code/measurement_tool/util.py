# utility methods to help run a measurement study

import subprocess
import base64
import json
import requests
import dns.message
import re
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from geopy.exc import GeocoderTimedOut

def traceroute_parse(data):
    trace_list = []
    for d in data:
        current_trace = []
        for x in d['result']:
            if 'from' in x['result'][0].keys() and 'rtt' in x['result'][0].keys():
                current_trace.append(str(x['hop']) + ": " + str(x['result'][0]['from']) + " " + str(x['result'][0]['rtt']))
            else:
                current_trace.append(str(x['hop']) + ": ***")
        trace_list.append(current_trace)
    return trace_list

def dns_parse(data):
    ip_list = []
    for d in data:
        for r in d['resultset']:
            if 'result' in r.keys():
                dnsmessage = str(dns.message.from_wire((base64.b64decode(r['result']['abuf']))))
                for dnsm in dnsmessage.split(";"):
                    if 'ANSWER' in dnsm:
                        for l in dnsm.split("\n")[1:-1]:
                            ip_list.append(l.split(" ")[-1])
            else:
                print "dns error"
    return ip_list

def curl(domain):
    try:
        page = subprocess.check_output("ssh princeton_stormship@planetlab2.pop-mg.rnp.br curl -k -L " + domain, stderr=subprocess.STDOUT, shell=True)
        return page
    except Exception as detail:
        f = open('log.txt', 'a')
        f.write('CURL: ' + domain + ' could not be fetched - ' + str(detail) + '\n')
        f.close()
        return ""

def extract_urls(page):
    urls = re.findall('src=\"http[\'"]?([^\'" >]+)', page)
    domains = []
    for u in urls:
        domains.append('http' + u)
    return domains

# TODO: update to use probes.txt
def run_DNS_measurements(urls):
    ip_list = []
    for u in urls:
        # Send this command (but fix quotations first and add <DOMAIN>)
        # Also, implement some sort of "wait-until-measurement-is-done" before curling the response
        #s = 'curl -H "Content-Type: application/json" -H "Accept: application/json" -X POST -d '
        #s += "'{ "
        #s += '"definitions": [ { "query_class": "IN", "query_type": "A", "query_argument": "' + u + '", "description": "DNS measurement to ' + u  + '", "type": "dns", "af": 4, "use_probe_resolver": true, "is_oneoff": true } ], "probes": [ { "requested": 2, "type": "probes", "value": "3363,15800" } ] }'
        #s += "' https://atlas.ripe.net/api/v1/measurement/?key=fc3f4123-89ce-4e9e-9c01-425182696abd"
        #response = subprocess.check_output(s, stderr = subprocess.STDOUT, shell=True)

        #temp = response.split(":")[-1]
        #measurement_list = temp[1:-2].split(",")
        measurement_list = ['2850269']
        for m in measurement_list:
            x = requests.get("https://atlas.ripe.net/api/v1/measurement/" + m  +  "/result/",)
            data = json.loads(x.text)
            ip_list.extend(dns_parse(data))
    return list(set(ip_list))

# TODO: update to use probes.txt
def run_traceroute_measurements(ips):
    traceroute_list = []
    ips.append('216.58.222.41')
    for ip in ips:
        # Send this command (but fix quotations first and add <IPADDRESS>)
        # Also, implement some sort of "wait-until-measurement-is-done" before curling the response
        #s = 'curl -H "Content-Type: application/json" -H "Accept: application/json" -X POST -d '
        #s += "'{ "
        #s += '"definitions": [ { "target": "' + ip + '", "protocol": "ICMP", "description": "Traceroute measurement to ' + ip + '", "type": "traceroute", "af": 4, "is_oneoff": true } ], "probes": [ { "requested": 2, "type": "probes", "value": "3363,15800" } ] }'
        #s += "' https://atlas.ripe.net/api/v1/measurement/?key=fc3f4123-89ce-4e9e-9c01-425182696abd"
        #response = subprocess.check_output(s, stderr = subprocess.STDOUT, shell=True)

        #temp = response.split(":")[-1]
        #measurement_list = temp[1:-2].split(",")
        measurement_list = ['2853537']
        for m in measurement_list:
            x = requests.get("https://atlas.ripe.net/api/v1/measurement/" + m  +  "/result/",)
            data = json.loads(x.text)
            traceroute_list.extend(traceroute_parse(data))
    return traceroute_list

def get_geo_distances(countries):
    geolocator = Nominatim()
    br = geolocator.geocode('BR', timeout=10)
    br_coord = (br.latitude, br.longitude)
    dist_map = {}
    for c in countries:
        print c
        location1 = geolocator.geocode(c, timeout=10)
        loc1_coord = (location1.latitude, location1.longitude)
        dist_map[c] = float(vincenty(loc1_coord, br_coord).miles)
    return dist_map

def geo_dist(x, y):
    geolocator = Nominatim()
    try:
        location1 = geolocator.geocode(x, timeout=10)
        location2 = geolocator.geocode(y, timeout=10)
        loc1 = (location1.latitude, location1.longitude)
        loc2 = (location2.latitude, location2.longitude)
        return vincenty(loc1, loc2).miles
    except GeocoderTimedOut as e:
        print("Error: geocode failed on input %s,%s"%(x,y))
        return 0

# naive geolocation tool based on RTT
def get_country_level_paths(traceroutes):
    f = open('anomalous_ips.txt', 'a')

    # 1. Look up all IP addresses in Team Cymru
    ips = []
    for trace in traceroutes:
        for t in trace:
            ip = t.split(" ")[1].strip()
            if ip != '***':
                ips.append(ip)
    ip_list = list(set(ips))

    f3 = open('netcat_temp.txt', 'w')
    f3.write('begin\n')
    f3.write('verbose\n')
    for ip in ip_list:
        f3.write(ip + '\n')
    f3.write('end\n')
    f3.close()

    command = ('netcat whois.cymru.com 43 < netcat_temp.txt | sort -n > list02')
    r = subprocess.Popen(command, shell=True)
    r.wait()

    ip_cc_map = {}
    c_list = []
    f_temp = open('list02', 'r')
    for line in f_temp:
        if line.split("|")[0].strip().isdigit() or line.split("|")[0].strip() == 'NA':
            if line.split("|")[1].strip() in ip_cc_map:
                ip_cc_map[line.split("|")[1].strip()].append(line.split("|")[3].strip())
            else:
                ip_cc_map[line.split("|")[1].strip()] = [line.split("|")[3].strip()]

            if line.split("|")[3].strip() != '':
                c_list.append(line.split("|")[3].strip())
    f_temp.close()

    countries = list(set(c_list))
    dist_map = get_geo_distances(countries)

    country_paths = []
    for trace in traceroutes:
        c_path = []
        # 1. Look up countries in map for whole trace
        for t in trace:
            if t.split(" ")[1].strip() != '***':
                cc = ip_cc_map[t.split(" ")[1].strip()][0]
                c_path.append(cc)
            else:
                c_path.append('***')

        domestic_rtt = ''
        for i in range(0, len(trace)):
            if c_path[i].strip() == 'BR':
                if trace[i].split(" ")[2].strip() != '':
                    domestic_rtt = trace[i].split(" ")[2].strip()
                    break

        if domestic_rtt != '':
            # 2. Check if RTT matches country (sequence ABA with no significant change in RTT)
            new_path = []
            for i in range(0,len(trace)):
                new_line = ''
                if i > 0:
                    pass_check = True
                    if trace[i].split(" ")[1] == '***':
                        new_line = trace[i].strip()
                    elif c_path[i] == '':
                        new_line = trace[i].strip()
                    elif (float(float(trace[i].split(" ")[2].strip()) - float(domestic_rtt)) > 60.0) and (float(dist_map[c_path[i]]) < 900.0): 
                        # rtt_diff large and geo_dist small
                        pass_check = False
                        # check country sequence (either there must be a cc change at this hop or the next hop)
                        if c_path[i] != c_path[i-1]:
                            pass_check = True
                        if i < len(trace) - 1:
                            if c_path[i] != c_path[i + 1]:
                                pass_check = True
                    elif (float(float(trace[i].split(" ")[2].strip()) - float(domestic_rtt)) < 60.0) and (float(dist_map[c_path[i]]) > 900.0):
                        # rtt_diff small and geo_dist large (should be domestic)
                        c_path[i] = 'BR'
                    if not pass_check:
                        f.write(trace[i].split(" ")[1].strip() + '\n')
                        new_line = trace[i]
                    else:
                        new_line = trace[i].strip() + ' ' + c_path[i]
                else:
                    new_line = trace[i].strip() + ' ' + c_path[i]
                new_path.append(new_line)
            country_paths.append(new_path)
        else:
            f_non_brazil = open('non_brazil_traces.txt', 'a')
            for tr in trace:
                f_non_brazil.write(tr + '\n')
            f_non_brazil.close()
    f.close()
    return country_paths

# store each traceroute file with a measurement run ID
def store(data, measurementID):
    f = open('run_' + str(measurementID), 'w')
    for d in data:
        for d2 in d:
            f.write(d2 + '\n')
        f.write('*\n')
    f.close()
