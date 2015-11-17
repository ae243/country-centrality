# utility methods to help run a measurement study

import subprocess
import base64
import json
import requests
import dns.message
import re

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

# TODO: use verisign's tool to do geolocation
def get_country_level_paths(traceroutes):
    # See measurements/as_country.py for details or provided by Verisign
    return []

# TODO: how/where should I store data
def store(data):
    # Figure out how to store all the traceroutes (and logs too) - some sort of structure or database
    print "STORE"

