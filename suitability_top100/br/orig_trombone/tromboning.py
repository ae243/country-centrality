import sys

trombone_count = 0
total_count = 0
domestic_count = 0
f = open('brazil_local_cc_paths.txt', 'r')
for line in f:
    if len(line.split("|")) > 1:
        countries = line.strip().split("|")[1:]
        if countries[0] == 'Brazil' or countries[0] == 'BR':
            if countries[-1].strip() == 'Brazil' or countries[-1].strip() == 'BR':
                domestic_count += 1
                if len(list(set(countries))) > 1:
                    trombone_count += 1
        total_count += 1

print trombone_count
print domestic_count
print total_count
