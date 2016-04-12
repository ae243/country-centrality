import sys

f = open('all_probe_pref.txt', 'r')
f2 = open('probe_subnets.txt', 'w')
for line in f:
    pref = line.split(" ")[1].strip()
    if pref != 'None':
        f2.write(pref + '\n')
f.close()
f2.close()
