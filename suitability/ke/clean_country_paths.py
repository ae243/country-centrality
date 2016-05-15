import sys

file_list = ['cc_brazil.txt', 'cc_brazil-vps.txt', 'cc_france.txt', 'cc_frankfurt.txt', 'cc_ireland.txt', 'cc_oregon.txt', 'cc_seoul.txt', 'cc_sydney.txt', 'cc_tokyo.txt', 'cc_spain.txt', 'cc_singapore.txt', 'cc_singapore-vps.txt']

for filename in file_list:
    f = open(filename, 'r')
    f2 = open('cleaned_' + filename, 'w')
    for line in f:
        items = line.split("|")
        new_string = ''
        for i in items:
            if i.strip() != 'None':
                new_string += (i.strip() + '|')
        new_string = new_string[:-1]
        if len(new_string.split("|")) > 1:
            f2.write(new_string + '\n')
    f2.close()
    f.close()
