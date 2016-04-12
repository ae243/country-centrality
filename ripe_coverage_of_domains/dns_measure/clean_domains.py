import sys

f = open('domains.txt', 'r')
new = []
for line in f:
    if line[:3] != 'www':
        temp = line[7:]
        if temp[:3] != 'www':
            new_domain = 'www.' + line[7:]
            new.append(new_domain)
        else:
            new.append(temp)
    else:
        new.append(line)

unique = list(set(new))

f_res = open('cleaned_domains.txt', 'w')
for u in unique:
    f_res.write(u)
f_res.close()
