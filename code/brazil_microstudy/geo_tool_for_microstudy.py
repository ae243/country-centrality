import util

geo_map = {}
f_geo = open('../data/openipmap.mappings.csv', 'r')
for line in f_geo:
    ip = line.split(',')[0]
    cc = line.split(',')[5]
    geo_map[ip] = cc

f = open('brazil_study_traceroutes.txt', 'r')
traceroutes = []
current_trace = []
for line in f:
    if line.split(" ")[0].strip() == '#':
        traceroutes.append(current_trace)
        current_trace = []
    elif line.split(':')[0].strip() == '1':
        traceroutes.append(current_trace)
        current_trace = [line.strip()]
    else:
        current_trace.append(line.strip())

c_paths = util.get_country_level_paths(traceroutes)
util.store(c_paths, 'test')
