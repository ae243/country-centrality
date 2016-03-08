import sys
import subprocess

domains = []
f = open('cleaned_domains.txt', 'r')
for line in f:
    domains.append(line.strip())
f.close()

count = 0
f_res = open('relay_domain_' + sys.argv[1] + '.txt', 'w')
for d in domains:
    traceroute = subprocess.Popen(["traceroute", d],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    traceroute.wait()
    for line in iter(traceroute.stdout.readline,""):
        f_res.write(line)
    count += 1
f_res.close()
