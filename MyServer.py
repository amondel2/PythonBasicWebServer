from http.server import BaseHTTPRequestHandler
import query_string
import json

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        url = self.address_string() + self.path
        dwqdwqd = query_string.parse(url)
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        for key, value in dwqdwqd.items():
            self.wfile.write(bytes(key, "utf-8"))
            self.wfile.write(bytes("=", "utf-8"))
            self.wfile.write(bytes(value, "utf-8"))
            self.wfile.write(bytes("<br >", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        data_dict = json.loads(post_body)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("{\n", "utf-8"))
        str = ""
        for key, value in data_dict.items():
            str += f'"{key}":"{value}",\n'
        self.wfile.write(bytes(f"{str[0:-2]}\n" + '}', "utf-8"))
