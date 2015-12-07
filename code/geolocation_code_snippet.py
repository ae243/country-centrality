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
