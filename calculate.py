from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
from Prod_list_clas import ProductService

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(SimpleHTTPRequestHandler, self).end_headers()

    def calc (self, post_data):
        # logging.error( post_data)
        name = "apple"
        amount = 34
        service = ProductService()
        item = service.request_func(name, amount)
        return item

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:63342')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.end_headers()
        self.wfile.write( str.encode(self.calc(post_data.decode('utf-8')).toJSON()))


httpd = HTTPServer(('localhost', 8001), SimpleHTTPRequestHandler)
httpd.serve_forever()
