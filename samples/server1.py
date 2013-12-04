import BaseHTTPServer

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('localhost', 8080)  
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    #print 'hi', handler_class.command

def run_while_true(server_class=BaseHTTPServer.HTTPServer,
                   handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    """
    This assumes that keep_running() is a function of no arguments which
    is tested initially and after each request.  If its return value
    is true, the server continues.
    """
    server_address = ('localhost', 8080)
    httpd = server_class(server_address, handler_class)
    while keep_running():
        httpd.handle_request()

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Hello!")

    def do_POST(self):
        print self.rfile.read()    
        

run(handler_class=Handler)    
#run_while_true()