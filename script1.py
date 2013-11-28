import BaseHTTPServer

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def run_while_true(server_class=BaseHTTPServer.HTTPServer,
                   handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    """
    This assumes that keep_running() is a function of no arguments which
    is tested initially and after each request.  If its return value
    is true, the server continues.
    """
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    while keep_running():
        httpd.handle_request()

run()    
#run_while_true()