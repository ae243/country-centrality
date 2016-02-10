import sys

# usage: python get_country_level_paths.py <ip to country map> <trace1> <trace2> <trace3> <trace4>

def analyze_path(ip_path, country_map):
    new_path = []
    for ip in ip_path:
        if ip.strip() != '***':
            new_path.append(country_map[ip])
    return new_path

f_ip_map = open(sys.argv[1], 'r')
ip_country_map = {}
for line in f_ip_map:
    ip = line.split(" ")[0]
    country = line.split(" ")[3].split("-")[0]
    ip_country_map[ip] = country

f_traces = open(sys.argv[2], 'r')
current_trace = []
country_level_paths = []
for line in f_traces:
    if line.split(":")[0] == '1':
        country_level_paths.append(analyze_path(current_trace, ip_country_map))
        ip = line.split(" ")[1]
        current_trace = [ip]
    else:
        ip = line.split(" ")[1]
        current_trace.append(ip)

f_results = open('country_paths.txt', 'w')
for path in country_level_paths:
    s = ' '.join(path)
    f_results.write(s + '\n')
f_results.close()
