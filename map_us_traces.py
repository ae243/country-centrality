import geoip2
import sys

f = open(sys.argv[1], 'r')
reader = geoip2.database.Reader('GeoIP2-City_20160830/GeoIP2-City.mmdb')
paths = []
cc_path = []
for line in f:
    if line.split(" ")[0] == 'src':
        paths.append(cc_path)
        cc_path = []
    if line.split(":")[0].strip().isdigit():
        ip = line.split(" ")[1].strip()
        res = reader.city(ip)
        cc = res.country.name
        if cc != 'None' and cc != None:
            cc_path.append(cc)
f.close()

f = open(sys.argv[2], 'w')
for p in paths:
    s = ','.join(p)
    f.write(s + "\n")
f.close()
