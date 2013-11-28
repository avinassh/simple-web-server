import time
import BaseHTTPServer
import urlparse
import urllib 

HOST_NAME = 'localhost'
PORT_NUMBER = 8089


class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """ Respond to a GET request. """
        
        #add a class to return stuff
        vm_number = 20
        vm_name = 'Cognitive Science'

        # self.send_response(200)
        # self.send_header("Content-type", "text/html")
        # self.end_headers()
        self.do_HEAD()

        if self.path == '/vmnum/':
            self.wfile.write("<html><head><title>One VM Per Lab</title></head>")
            self.wfile.write("<body><p>Success!</p>")
            self.wfile.write("<p>Currently there are %s virtual machines are running" % vm_number)
            self.wfile.write("<p>You accessed path: %s</p>" % self.path)
            self.wfile.write("</body></html>")
        elif self.path == '/vmname/':
            self.wfile.write("<html><head><title>One VM Per Lab</title></head>")
            self.wfile.write("<body><p>Success!</p>")
            self.wfile.write("<p>Current VM name is %s" % vm_name)
            self.wfile.write("<p>You accessed path: %s</p>" % self.path)
            self.wfile.write("</body></html>")
        else:
            self.wfile.write("<html><head><title>One VM Per Lab</title></head>")
            self.wfile.write("<body><p>This is a test.</p>")
            self.wfile.write("<p>You accessed path: %s</p>" % self.path)
            self.wfile.write("</body></html>") 
        # reply back in JSON
        # 
        return
            

    def do_POST(self):
        """ Respond to a POST request """
        length = int(self.headers['Content-Length'])
        #http://stackoverflow.com/a/12731208/1382297
        post_data = urlparse.parse_qs(self.rfile.read(length).decode('utf-8'))
        lab_name = str(post_data.get('lab-name')[0])
        lab_author = str(post_data.get('lab-author')[0])
        #print "%s/?%s" % (self.path, urllib.urlencode(post_data))
        #print "%s/?%s" % (self.path, urllib.urlencode({k:v[0] for k,v in post_data.iteritems()}))
        self.wfile.write("<html><head><title>One VM Per Lab</title></head>")
        self.wfile.write("<body><p>This is a test.</p>")
        self.wfile.write("<p>You successfully created a VM named: %s at the location: %s</p>" % (lab_name, lab_author))
        self.wfile.write("</body></html>")        
        return    


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), Handler)
    print "Server Started - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    print "Server Stopped - %s:%s" % (HOST_NAME, PORT_NUMBER)