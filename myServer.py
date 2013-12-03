import time
import BaseHTTPServer
import urlparse
import urllib 
import SocketServer
import threading

HOST_NAME = 'localhost'
PORT_NUMBER = 8089


class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """ Respond to a GET request. """

        # self.do_HEAD() HEAD shouldn't be called from here!
        # rather construct same message here 

        if self.path == '/vmnum/':
            response = self.construct_message('Currently there are no VMs running')
            self.wfile.write(response)
        elif self.path == '/vmname/':
            respose = self.construct_message('Your VM is yet to be named')
            self.wfile.write(respose)
        else:
            response = self.construct_message()
            self.wfile.write(response)
        return
            

    def do_POST(self):
        """ Respond to a POST request """
        length = int(self.headers['Content-Length'])

        #http://stackoverflow.com/a/12731208/1382297
        post_data = urlparse.parse_qs(self.rfile.read(length).decode('utf-8'))
        thread_number = threading.currentThread().getName()
        lab_name = str(post_data.get('lab-name')[0])
        lab_author = str(post_data.get('lab-author')[0])
        
        #print "%s/?%s" % (self.path, urllib.urlencode(post_data))
        #print "%s/?%s" % (self.path, urllib.urlencode({k:v[0] for k,v in post_data.iteritems()}))

        message = "<p>You successfully created a VM named: " + lab_name + " at the location: " + lab_author + "</p><p>\
        \nYou have been served from the thread: " + thread_number
        respose = self.construct_message(message)

        self.wfile.write(respose)
        return

    def construct_message(self, message=''):
        message_part1 = "<html><head><title>One VM Per Lab</title></head><body><p>Success!</p>"
        message_part2 = "<p>You accessed path: " + self.path + "</p>"
        message_part3 = "</body></html>"
        return message_part1 + message_part2 + message + message_part3

class ThreadedHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    """Handle requests in a separate thread."""
    pass

if __name__ == '__main__':
    #httpd = server_class((HOST_NAME, PORT_NUMBER), Handler)
    httpd = ThreadedHTTPServer((HOST_NAME, PORT_NUMBER), Handler)
    try:
        print "Server Started - %s:%s with the thread :%s" % (HOST_NAME, PORT_NUMBER, server_thread.name)
        # server_thread = threading.Thread(target=httpd.serve_forever)
        # Exit the server thread when the main thread terminates
        # server_thread.daemon = True
        # server_thread.start()
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    print "Server Stopped - %s:%s" % (HOST_NAME, PORT_NUMBER)