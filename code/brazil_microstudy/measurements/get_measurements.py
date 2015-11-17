import sys
import requests
import json

fb_measurements = ['2853131', '2853138']
google_measurements = ['2853221', '2853224', '2853228', '2853231', '2853236', '2853240', '2853243', '2853247', '2853250', '2853254', '2853258', '2853262', '2853265']
youtube_measurements = ['2853273', '2853277', '2853282', '2853286', '2853288', '2853292', '2853296', '2853299', '2853303', '2853307', '2853309', '2853312']
yahoo_measurements = ['2853176', '2853183', '2853182']
twitter_measurements = ['2853191', '2853190', '2853201', '2853206']
wiki_measurements = ['2853036']
blogspot_measurements = ['2853113', '2853112', '2853119', '2853121', '2853125']
bing_measurements = ['2853040']
amazon_measurements = ['2853145', '2853150', '2853155']
live_measurements = ['2853429', '2853436', '2853435', '2853442', '2853441', '2853450', '2853449', '2853456', '2853455', '2853458', '2853465', '2853464']
linkedin_measurements = ['2852999', '2853030']
ebay_measurements = ['2853062', '2853068', '2853071', '2853075', '2853078', '2853091', '2853096', '2853100', '2853104']
instagram_measurements = ['2853473', '2853497', '2853496', '2853495', '2853494', '2853493', '2853492', '2853491', '2853490', '2853543', '2853542', '2853541', '2853540', '2853539', '2853538', '2853537', '2853536', '2853584', '2853583', '2853582', '2853581', '2853580', '2853579', '2853578', '2853577']
uol_measurements = ['2853161', '2853167']
globo_measurements = ['2853055']
mercadolivre_measurements = ['2853050', '2853049']

measurements = [fb_measurements, google_measurements, youtube_measurements, yahoo_measurements, twitter_measurements, wiki_measurements, blogspot_measurements, bing_measurements, amazon_measurements, live_measurements, linkedin_measurements, ebay_measurements, instagram_measurements, uol_measurements, globo_measurements, mercadolivre_measurements]

domains = ['facebook', 'google', 'youtube', 'yahoo', 'twitter', 'wikipedia', 'blogspot', 'bing', 'amazon', 'live', 'linkedin', 'ebay', 'instagram', 'uol', 'globo', 'mercadolivre']

f = open(sys.argv[1], 'w')

i = 0
for m in measurements:
	f.write('# ' + domains[i] + '\n')
	for m2 in m:
		#command = 'curl https://atlas.ripe.net/api/v1/measurement/'+ m2 + '/result/ > temp.txt'
		#r = subprocess.Popen(command, shell=True)
		#with open('temp.txt', 'r') as data_file:
    		#	data = json.load(data_file)
		# parse r (keep in mind r might be multiple traceroutes or a single traceroute
		# write parsed r to f
		r = requests.get('https://atlas.ripe.net/api/v1/measurement/' + m2 + '/result/')
		data = json.loads(r.text)
		for res in range(0, len(data)):
			for x in data[res]['result']:
        			if 'from' in x['result'][0].keys() and 'rtt' in x['result'][0].keys():
                			f.write(str(x['hop']) + ": " + str(x['result'][0]['from']) + " " + str(x['result'][0]['rtt']) + "\n")
        			else:
                			f.write(str(x['hop']) + ": ***\n")
	i += 1

f.close()

