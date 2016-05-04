import sys

trombone_count = 0
total_count = 0
domestic_count = 0
f = open('us_local_cc_paths.txt', 'r')
for line in f:
    if len(line.split("|")) > 1:
        countries = line.strip().split("|")[1:]
        if countries[0] == 'United States' or countries[0] == 'US':
            if countries[-1].strip() == 'United States' or countries[-1].strip() == 'US':
                domestic_count += 1
                if len(list(set(countries))) > 1:
                    trombone_count += 1
        total_count += 1

print trombone_count
print domestic_count
print total_count
