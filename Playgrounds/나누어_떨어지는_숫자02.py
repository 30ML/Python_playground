from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as parser


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()

        f = open("index.html", "r")
        data = f.read()
        f.close()
