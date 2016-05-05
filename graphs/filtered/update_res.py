import sys

f = open(sys.argv[1], 'r')
f_res = open(sys.argv[2], 'w')
total_paths = 0
for line in f:
    if len(line.split(",")) < 2:
        total_paths = int(line.strip())
    else:
        items = line.split(",")
        country = items[0]
        t = items[1]
        h = items[2]
        f_res.write(country + "," + t + "," + h + "," + str(float(h)/float(total_paths)) + '\n')
f_res.close()
f.close()
