import sys

def check_tromboning(trace):
    c_path = []
    for t in trace:
        if len(t.split(" ")) > 3:
            c_path.append(t.split(" ")[3].strip())

    for c in c_path:
        if c_path[0] == 'BR' and c_path[-1] == 'BR':
            if c != 'BR':
                return True
    return False

f = open(sys.argv[1], 'r')
f2 = open('tromboning_traces.txt', 'w')
current_trace = []
tromboning_count = 0
total = 0
for line in f:
    if line.strip() == '*':
        # analyze current trace
        res = check_tromboning(current_trace)
        if res:
            for tr in current_trace:
                f2.write(tr + '\n')
            f2.write("*\n")
            tromboning_count += 1
        current_trace = []
        total += 1
    else:
        current_trace.append(line.strip())
f.close()
f2.close()
print str(tromboning_count) + " traces trombone.\n"
print str(total) + " total traces.\n"
