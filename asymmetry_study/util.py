# utility methods to help run a measurement study

import subprocess
import base64
import json
import requests
import dns.message
import re
import datetime
import time
import ipaddr
import netaddr
import sys

def consolidate_ips(ips):
    subnet_map = {} # map of <subnet, list of IPs in subnet>
    for ip in ips:
        x = netaddr.IPNetwork(ip)
        real_sub = x.supernet(24)[0]
        if real_sub in subnet_map:
            subnet_map[real_sub] += ip
        else:
            subnet_map[real_sub] = [ip]

    new_ips = []
    print str(len(ips)) + " original ip addresses"
    print str(len(subnet_map)) + " consolidated ip addresses"
    for s in subnet_map:
        new_ips.append(subnet_map[s][0])
    return new_ips

def traceroute_parse(data):
    trace_list = []
    for d in data:
        try:
	    current_trace = []
            for x in d['result']:
                if 'from' in x['result'][0].keys() and 'rtt' in x['result'][0].keys():
                    current_trace.append(str(x['hop']) + ": " + str(x['result'][0]['from']) + " " + str(x['result'][0]['rtt']))
                else:
                    current_trace.append(str(x['hop']) + ": ***")
            trace_list.append(current_trace)
        except:
            f = open('log.txt', 'a')
            f.write('Traceroute analysis failed: ' + str(data) + '\n')
            f.close()
    return trace_list

def dns_parse(data):
    ip_list = []
    for d in data:
	try:
            for r in d['resultset']:
                if 'result' in r.keys():
                    dnsmessage = str(dns.message.from_wire((base64.b64decode(r['result']['abuf']))))
                    for dnsm in dnsmessage.split(";"):
                        if 'ANSWER' in dnsm:
                            for l in dnsm.split("\n")[1:-1]:
                                if l.split(" ")[-2] == 'A':
                                    ip_list.append(l.split(" ")[-1])
                else:
                    print "dns error"
	except TypeError:
            f = open('log.txt', 'a')
            f.write('DNS analysis failed: ' + str(data) + '\n')
            f.close()
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

def clean_targets(targets):
    clean = []
    for t in targets:
        if t[0:5] == 'https':
            t = t[8:]
        elif t[0:4] == 'http':
            t = t[7:]	
        clean.append(t.split("/")[0].strip())
    return clean

def get_probes():
    f = open('probes.txt', 'r')
    s = ''
    for line in f:
        s += line.strip() + ','
    f.close()
    return s[:-1]

def get_probes_count():
    f = open('probes.txt', 'r')
    count = 0
    for line in f:
        count += 1
    f.close()
    return count

def run_DNS_measurements(urls):
    measurement_list = []
    counter = 1
    for u in urls:
        if counter >= 99:
            time.sleep(600)
            counter = 1
        s = 'curl -H "Content-Type: application/json" -H "Accept: application/json" -X POST -d '
        s += "'{ "
        s += '"definitions": [ { "query_class": "IN", "query_type": "A", "query_argument": "' + u.strip() + '", "description": "DNS measurement to ' + u.strip()  + '", "type": "dns", "af": 4, "use_probe_resolver": true, "is_oneoff": true } ], "probes": [ { "requested": ' + str(get_probes_count()) + ', "type": "probes", "value": "' + get_probes() + '" } ] }'
        s += "' https://atlas.ripe.net/api/v1/measurement/?key=fc3f4123-89ce-4e9e-9c01-425182696abd"
        response = subprocess.check_output(s, stderr = subprocess.STDOUT, shell=True)
        temp = response.split(":")[-1]
        measurement_list.extend(temp[1:-2].split(","))
        counter += 1
    return measurement_list

def analyze_DNS_measurements(id_list):
    ip_list = []
    for measurement in id_list:
        if measurement.isdigit():
            x = requests.get("https://atlas.ripe.net/api/v1/measurement/" + str(measurement) +  "/result/",)
            data = json.loads(x.text)
            ip_list.extend(dns_parse(data))
    return list(set(ip_list))

def check_statuses(measurement_list):
    for m in measurement_list:
        if m.isdigit():
            s = requests.get("https://atlas.ripe.net/api/v1/measurement/" + str(m) + "/?status",)
            data = json.loads(s.text)
            try:
                if data['status']['name'] == 'Failed':
                    return True
                elif data['status']['name'] != 'Stopped':
                    return False
            except:
                return True
    return True

def run_traceroute_measurements(ips, type):
    measurement_list = []
    counter = 1
    for ip in ips:
        if counter >= 99:
            time.sleep(900)
            while not check_statuses(measurement_list):
                print "NEED MORE SLEEP"
                time.sleep(300)    
            counter = 1
        s = 'curl -H "Content-Type: application/json" -H "Accept: application/json" -X POST -d '
        s += "'{ "
        s += '"definitions": [ { "target": "' + ip.strip() + '", "protocol": "' + type + '", "paris": 16, "description": "Traceroute measurement to ' + ip.strip() + '", "type": "traceroute", "af": 4, "is_oneoff": true } ], "probes": [ { "requested": ' + str(get_probes_count()) + ', "type": "probes", "value": "' + get_probes() + '" } ] }'
        s += "' https://atlas.ripe.net/api/v1/measurement/?key=fc3f4123-89ce-4e9e-9c01-425182696abd"
        response = subprocess.check_output(s, stderr = subprocess.STDOUT, shell=True)
        temp = response.split(":")[-1]
        measurement_list.extend(temp[1:-2].split(","))
        counter += 1
    return measurement_list

def analyze_traceroute_measurements(id_list):
    traceroute_list = []
    for measurement in id_list:
        if measurement.isdigit():
            x = requests.get("https://atlas.ripe.net/api/v1/measurement/" + str(measurement)  +  "/result/",)
            data = json.loads(x.text)
            traceroute_list.extend(traceroute_parse(data))
    return traceroute_list

def start_dest(data):
    trace_map = {}
    for d in data:
        try:
            current_trace = []
            if 'from' in d.keys() and 'dst_name' in d.keys():
                current_s_d = (d['from'], d['dst_name'])
                current_trace = []
                for x in d['result']:
                    if 'from' in x['result'][0].keys() and 'rtt' in x['result'][0].keys():
                        current_trace.append(str(x['hop']) + ": " + str(x['result'][0]['from']) + " " + str(x['result'][0]['rtt']))
                    else:
                        current_trace.append(str(x['hop']) + ": ***")
                trace_map[current_s_d] = current_trace
        except:
            f = open('log.txt', 'a')
            f.write('Traceroute start_dest analysis failed: ' + str(data) + '\n')
            f.close()
    return trace_map

def get_start_dest_traceroute(id_list):
    start_dest_map = {}
    for measurement in id_list:
        if measurement.isdigit():
            x = requests.get("https://atlas.ripe.net/api/v1/measurement/" + str(measurement)  +  "/result/",)
            data = json.loads(x.text)
            start_dest_map.update(start_dest(data))
    return start_dest_map

# store each traceroute file with a measurement run ID
def store_traces(data):
    fmt='%Y-%m-%d-%H-%M-%S_{fname}'
    fname = 'traceroutes'
    f = open(datetime.datetime.now().strftime(fmt).format(fname=fname), 'w')
    for d in data:
        for d2 in d:
            f.write(d2 + '\n')
    f.close()

def store_domains(data):
    fmt='%Y-%m-%d-%H-%M-%S_{fname}'
    fname = 'domains'
    f = open(datetime.datetime.now().strftime(fmt).format(fname=fname), 'w')
    for d in data:
        s = ''
        for d2 in d:
            s += d2.strip() + ','
        f.write(s.strip() + '\n')
    f.close()
