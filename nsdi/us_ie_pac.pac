function FindProxyForURL(url, host){
if ((shExpMatch(host, "*.facebook.com")))
return "PROXY 199.195.193.17:3128";
if ((shExpMatch(host, "*.netflix.com")))
return "PROXY 205.204.85.12:3128";
if ((shExpMatch(host, "*.instagram.com")))
return "PROXY 119.252.188.33:3128";
if ((shExpMatch(host, "*.dropbox.com")))
return "PROXY 187.45.186.35:3128";
return "DIRECT";
}
