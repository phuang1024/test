from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write(self.path.encode())
        self.wfile.flush()
        
        
def main():
    server = HTTPServer(("", 80), Handler)
    server.serve_forever()
    
    
main()
