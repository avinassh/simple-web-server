import urllib2
req = urllib2.Request(url='http://localhost:8080')#, data='This is POST data')#,data='This data is passed to stdin of the CGI')
print urllib2.urlopen(req).read()
#print f.read()
#Got Data: "This data is passed to stdin of the CGI"
