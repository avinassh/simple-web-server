import urllib2
req = urllib2.Request(url='http://localhost:8000', data='This is POST data')#,data='This data is passed to stdin of the CGI')
urllib2.urlopen(req)
#print f.read()
#Got Data: "This data is passed to stdin of the CGI"