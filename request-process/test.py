from kivy.network.urlrequest import UrlRequest

req=UrlRequest(url,ca_file=certifi.where(),verify=False)
req.wait()
