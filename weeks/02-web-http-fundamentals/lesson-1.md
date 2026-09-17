# Lesson 1 — How the Web Works

## Client and server

A **client** (a browser, `curl`, a mobile app) sends a **request** to a
**server**, which sends back a **response**. This matters because every
backend you build for the rest of this course is a server — its whole
job is receiving requests and returning responses.

```
Client  ──request──▶  Server
Client  ◀─response──  Server
```

**Task:** Open your browser's dev tools (F12 → Network tab), visit any
website, and find one request. Identify: the URL, the method, and the
status code.

## A first look at a request and a response

A request has a **method** (what kind of action), a **path** (which
resource), **headers** (metadata), and sometimes a **body** (data being
sent). A response has a **status code** (did it work?), headers, and
usually a body (the actual content).

```
GET /products/42 HTTP/1.1
Host: example.com

HTTP/1.1 200 OK
Content-Type: application/json

{"id": 42, "name": "Coffee Mug"}
```

**Common error (conceptual):** confusing the *path* (`/products/42`)
with the full URL (`https://example.com/products/42`) — the path is
just the part after the domain, and it's what your server code actually
sees and routes on.

## Checkpoint

What are the four parts of a request listed above? (Method, path,
headers, body.)

## Independent challenge

Pick three different websites. In dev tools, find one GET request on
each and note its status code. Are they all 200? If not, why might a
site intentionally return something else (e.g. a redirect)?
