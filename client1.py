import urllib2
from urllib import urlencode

payload_sample_1 = urlencode({'name':'John Appleseed', 'location': '1 Infinite Loop'})
payload_sample_2 = urlencode({'name':'John Samsung', 'location': 'North Korea'})

req = urllib2.Request(url='http://localhost:8089', data=payload_sample_1)#,data='This data is passed to stdin of the CGI')
print urllib2.urlopen(req).read()
#print f.read()
#Got Data: "This data is passed to stdin of the CGI"

#HTTPClientRequest
#__init__ 
#create_request(JSON)
#execute_request

#CSPF attack token/session cookie
