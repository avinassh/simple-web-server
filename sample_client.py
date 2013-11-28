from HTTPClientRequest import *

fn = open(sys.argv[1], 'r')
json_file = fn.read()
fn.close()

HOST_NAME = 'http://localhost'
PORT_NUMBER = '8089'

my_request = HTTPClientRequest(json_file, HOST_NAME, PORT_NUMBER)

#my_request.create_request(json_file)
my_request.execute_request()