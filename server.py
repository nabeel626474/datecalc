import http.server
import socketserver
import os
import urllib.parse

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class StaticSiteHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if '?' in self.path and '_rsc' in self.path:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{}')
            return

        if path != '/' and not os.path.splitext(path)[1]:
            html_path = path.lstrip('/') + '.html'
            if os.path.isfile(html_path):
                self.path = '/' + html_path
                if parsed.query:
                    self.path += '?' + parsed.query

        return super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

PORT = 5000
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", PORT), StaticSiteHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
