""" 
This creates an HTTPClientRequest object. The constructor receives the JSON 
file which contains the request. Then it creates the object with the data
specified from the JSON, builds the appropriate GET/POST URL. When Execute 
method is called, the request is sent to server
"""

import urllib2
from urllib import urlencode
import sys
import os

print sys.argv
