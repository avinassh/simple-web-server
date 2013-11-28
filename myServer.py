import time
import BaseHTTPServer


HOST_NAME = 'localhost'
PORT_NUMBER = 8080


class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """ Respond to a GET request. """
        
        vm_number = 20
        vm_name = 'Cognitive Science'

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == '/vmnum/':
            self.wfile.write("<html><head><title>One VM Per Lab</title></head>")
            self.wfile.write("<body><p>This is a test.</p>")
            self.wfile.write("<p>Currently there are %s virtual machines are running" % vm_number)
            self.wfile.write("<p>You accessed path: %s</p>" % self.path)
            self.wfile.write("</body></html>")
        elif self.path == '/vmname/':
            self.wfile.write("<html><head><title>One VM Per Lab</title></head>")
            self.wfile.write("<body><p>This is a test.</p>")
            self.wfile.write("<p>Current VM name is %s" % vm_name)
            self.wfile.write("<p>You accessed path: %s</p>" % self.path)
            self.wfile.write("</body></html>")
        else :
            self.wfile.write("<html><head><title>One VM Per Lab</title></head>")
            self.wfile.write("<body><p>This is a test.</p>")
            self.wfile.write("<p>You accessed path: %s</p>" % self.path)
            self.wfile.write("</body></html>")   
        return
            

    def do_POST(self):
        """ Respond to a POST request """
        pass    


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), Handler)
    print "Server Started - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print "Server Stopped - %s:%s" % (HOST_NAME, PORT_NUMBER)