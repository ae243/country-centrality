import subprocess
import sys
import util

measurement_ids = ['3375848']

traceroutes = util.analyze_traceroute_measurements(measurement_ids)

print "The number of traceroutes: "
print len(traceroutes)

ip_list = []
for t in traceroutes:
    for t2 in t:
        ip = t2.split(" ")[1]
        if ip.split('.')[0].strip().isdigit():
            ip_list.append(ip.strip())

f = open('netcat_temp.txt', 'w')
f.write('begin\n')
f.write('verbose\n')
for ip in ip_list:
    f.write(ip + '\n')
f.write('end\n')
f.close()

command = ('netcat whois.cymru.com 43 < netcat_temp.txt | sort -n > list02')
r = subprocess.Popen(command, shell=True)
r.wait()

ip_as_map = {}
f_temp = open('list02', 'r')
for line in f_temp:
    if line.split("|")[0].strip().isdigit():
        if line.split("|")[1].strip() in ip_as_map:
            ip_as_map[line.split("|")[1].strip()].append(line.split("|")[0].strip())
        else:
            ip_as_map[line.split("|")[1].strip()] = [line.split("|")[0].strip()]
f_temp.close()

for asn in ip_as_map:
    ip_as_map[asn] = list(set(ip_as_map[asn]))

as_paths = []
for t in traceroutes:
    as_path = ''
    for t2 in t:
        if t2.split(" ")[1].split('.')[0].isdigit() and t2.split(" ")[1] in ip_as_map:
            as_path += str(ip_as_map[t2.split(" ")[1]])
            as_path += " "
    as_paths.append(as_path)

print "The number of as paths: "
print len(as_paths)

#remove multiples of the same AS in the path

modified_as_paths = []
for as_path in as_paths:
    ases = as_path.split(" ")
    new_path = []
    for asn in ases:
        if not len(new_path) == 0:
            if not new_path[-1] == asn:
                new_path.append(asn)
        else:
            new_path.append(asn)
    string_new_path = ''
    for n in new_path:
        string_new_path += str(n)
        string_new_path += " "
    modified_as_paths.append(string_new_path)

as_path_set = list(set(modified_as_paths))

print "The number of unique as paths: "
print len(as_path_set)
for asn in as_path_set:
    print asn
