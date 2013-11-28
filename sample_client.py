from HTTPClientRequest import *

fn = open(sys.argv[1], 'r')
json_file = fn.read()
fn.close()

my_request = HTTPClientRequest(json_file)

my_request.create_request(json_file)
my_request.execute_request()