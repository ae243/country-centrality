import sys
import dns.resolver #import the module
myResolver = dns.resolver.Resolver() #create a new instance named 'myResolver'

domains = []
f = open('cleaned_domains.txt', 'r')
for line in f:
    domains.append(line.strip())
f.close()

f_log = open('fail.txt', 'w')
f_log2 = open('successful.txt', 'w')
for d in domains:
    try:
        myAnswers = myResolver.query(d, "A") #Lookup the 'A' record(s) for google.com
        for rdata in myAnswers: #for each response
            print rdata #print the data
            f_log2.write(d + '\n')
    except:
        f_log.write(d + '\n')
f_log.close()
f_log2.close()
