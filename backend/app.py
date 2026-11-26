from http.server import BaseHTTPRequestHandler, HTTPServer
import json

TODOS = [{"id": 1, "title": "Test task", "done": False}]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
        elif self.path == "/todos":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(TODOS).encode())
        else:
            self.send_response(404)
            self.end_headers()

HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
