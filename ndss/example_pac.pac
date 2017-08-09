function FindProxyForURL(url, host){
    if ((shExpMatch(host, "*.google.com")))
        return "PROXY 1.2.3.4:3128";
    if ((shExpMatch(host, "*.twitter.com")))
        return "PROXY 5.6.7.8:3128";
    return "DIRECT";
}
