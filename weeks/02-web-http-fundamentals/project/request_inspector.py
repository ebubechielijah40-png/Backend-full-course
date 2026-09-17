"""
Request Inspector
Week 2 project — Backend Development with Python & Django

A minimal HTTP server (standard library only) that logs and explains
every request it receives: method, path, query string, headers, and
body.

Run it with:
    python3 request_inspector.py
Then, in another terminal:
    curl -i "http://localhost:8000/hello?name=Eli"
    curl -i -X POST -d '{"name": "test"}' http://localhost:8000/items
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json


class InspectorHandler(BaseHTTPRequestHandler):
    def _explain(self, method, body=None):
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)

        print(f"\n--- {method} request received ---")
        print(f"Path: {parsed.path}")
        print(f"Query parameters: {query}")
        print("Headers:")
        for key, value in self.headers.items():
            print(f"  {key}: {value}")
        if body:
            print(f"Body: {body}")

        summary = {
            "method": method,
            "path": parsed.path,
            "query": query,
            "body": body,
        }
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(summary, indent=2).encode())

    def do_GET(self):
        self._explain("GET")

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(length).decode() if length else ""
        try:
            body = json.loads(raw_body) if raw_body else None
        except json.JSONDecodeError:
            body = raw_body  # not JSON — show the raw text instead
        self._explain("POST", body)

    def log_message(self, format, *args):
        # Silence the default access log; our own printing above is
        # clearer for teaching purposes.
        pass


if __name__ == "__main__":
    port = 8000
    print(f"Request Inspector listening on http://localhost:{port}")
    print("Press Ctrl+C to stop.\n")
    HTTPServer(("localhost", port), InspectorHandler).serve_forever()
