import http.server 
import redis

r = redis.Redis(host = 'redis', port=6379)
class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        if self.path =='/':
            r.incr('counter')

            self.wfile.write(b'This page has been visited %s Times !' % r.get('counter'))
server = http.server.HTTPServer(('localhost',8080), RequestHandler)
server.serve_forever()