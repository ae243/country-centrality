import sys

count = 0
is_subset = 0
is_same_set = 0
f = open('asymmetry_results_log.txt', 'r')
for line in f:
    x = line[1:-2].split("] [")
    if len(x) > 1:
        y = x[0][1:-1].split("', '")
        z = x[1][1:-1].split("', '")
        forward_set = set(y)
        reverse_set = set(z)
        if 'None' in forward_set:
            forward_set.remove('None')
        if 'None' in reverse_set:
            reverse_set.remove('None')
        if reverse_set <= forward_set:
            is_subset += 1
        if reverse_set == forward_set:
            is_same_set += 1
        count += 1

print is_same_set
print is_subset
print count
