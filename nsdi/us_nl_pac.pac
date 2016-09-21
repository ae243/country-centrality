function FindProxyForURL(url, host){
if ((shExpMatch(host, "*.comcast.net")))
return "PROXY 109.123.93.238:3128";
if ((shExpMatch(host, "*.diply.com")))
return "PROXY 176.67.169.185:3128";
if ((shExpMatch(host, "*.wikipedia.org")))
return "PROXY 50.31.252.80:3128";
if ((shExpMatch(host, "*.outbrain.com")))
return "PROXY 119.252.188.33:3128";
if ((shExpMatch(host, "*.weather.com")))
return "PROXY 187.45.186.35:3128";
return "DIRECT";
}
