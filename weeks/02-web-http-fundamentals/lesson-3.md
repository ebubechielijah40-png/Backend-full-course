# Lesson 3 — Serving Dynamic Content and Inspecting Real Traffic

## A minimal Python web server

Python's standard library can act as a server, without any framework.
This is worth seeing once so Django (starting next week) doesn't feel
like magic — it's doing the same fundamental thing, with far more
convenience.

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(f"You requested: {self.path}\n".encode())

HTTPServer(("localhost", 8000), Handler).serve_forever()
```

Run it, then visit `http://localhost:8000/anything` in a browser or with
`curl` — the response echoes back whatever path you requested.

**Common error:** `OSError: [Errno 98] Address already in use` means a
previous server instance is still running on that port — stop it (Ctrl+C
in its terminal) or pick a different port number.

## Building the Request Inspector

This week's project extends the server above to log method, path,
headers, and body for every request, and handle GET and POST
differently. See `project/README.md` for the full specification — the
core addition beyond the example above is reading `self.headers` and,
for POST, reading `self.rfile.read(content_length)` to get the body.

**Guided activity:** Add a `do_POST` method alongside `do_GET` that
reads and prints the request body.

**Task:** Send a POST request with a JSON body using `curl`:

```
curl -X POST -d '{"name": "test"}' http://localhost:8000/
```

Confirm your server logs the body correctly.

## Checkpoint

Why does a POST handler need to explicitly read the body's length before
reading the body itself, while a GET handler generally doesn't have a
body to read? (Because HTTP doesn't send a body boundary marker — the
server needs to know in advance, via the `Content-Length` header, how
many bytes to read.)

## Independent challenge

Extend your server to return a `404` response (not `200`) for any path
that isn't `/`, and confirm with `curl -i` that the status code changes
correctly.
