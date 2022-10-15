from http.server import HTTPServer, BaseHTTPRequestHandler


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write("<p>hello world</p>".encode())
        self.wfile.write(self.path.encode())
        self.wfile.write("<p>hello world</p>".encode())
        self.wfile.write("<p>hello world</p>".encode())

    def do_POST(self):
        pass


PORT = 8080
server = HTTPServer(("", PORT), ServerHandler)
print(f"서버가 {PORT}로 서비스되고 있습니다.")
server.serve_forever()
