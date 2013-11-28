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
import re
import json

HOST_NAME = 'http://localhost'
PORT_NUMBER = '8089'

class HTTPClientRequest(object):
    """docstring for HTTPClientRequest"""
    def __init__(self, request_specs):
        #self.create_request(request_specs)
        pass

    def create_request(self, request_specs):
        base_url = self._set_base_url(HOST_NAME, PORT_NUMBER)
        payload = self._convert_json_to_dict(request_specs)
        payload = self._encode_payload(payload)
        self.request_url = urllib2.Request(url=base_url, data=payload)

    def execute_request(self):
        print urllib2.urlopen(self.request_url).read()

    def _convert_json_to_dict(self, request_specs):
        return json.loads(request_specs)

    def _encode_payload(self, payload):
        return urlencode(payload)    

    def _set_base_url(self, HOST_NAME, PORT_NUMBER):
        return str(HOST_NAME+':'+PORT_NUMBER)


#valid_json_file = r'[a-zA-Z0-9\-]+\.json'

#fn = open(sys.argv[1], 'r')
#file_data = fn.read()

#dictio = json.loads(file_data)

#print re.search(valid_json_file, sys.argv[1])
#bool(re.match(valid_json_file, sys.argv[1]))
#re.find(valid_json_file, sys.argv[1])