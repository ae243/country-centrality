  $url = "http://example.com";
  $agent = "Mozilla/5.0 (X11; U; Linux i686; en-US) 
            AppleWebKit/532.4 (KHTML, like Gecko) 
            Chrome/4.0.233.0 Safari/532.4";
  $referer = "http://www.google.com/";

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_HTTPPROXYTUNNEL, 1);
  curl_setopt($ch, CURLOPT_PROXY, '202.95.141.129:8080');
  curl_setopt($ch, CURLOPT_REFERER, $referer);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
  curl_setopt($ch, CURLOPT_MAXREDIRS, 2);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
  curl_setopt($ch, CURLOPT_USERAGENT, $agent);
  
  $data = curl_exec($ch);
  curl_close($ch);
  echo $data;
