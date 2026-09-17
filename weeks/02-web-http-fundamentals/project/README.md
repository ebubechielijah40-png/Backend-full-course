# Project: Request Inspector

## Problem
Students have read *about* HTTP but haven't watched it happen. Nothing
here makes the request/response cycle concrete until they can see real
requests arriving.

## Purpose
Turn HTTP from an abstract diagram into something observed directly.

## Requirements
- A Python script using the standard library's `http.server` module.
- Accepts GET and POST requests.
- Logs, for each request: method, path, query string, headers, and body
  (if present).
- Responds with a plain-text or JSON summary of what it received.

## Features
- Distinguishes GET vs. POST and handles each appropriately.
- Echoes query-string parameters back in the response.
- Returns a 404-style response for unrecognized paths, and explains why.

## Expected user behavior
A student sends requests using a browser and a CLI HTTP client (e.g.
`curl`) and can predict what the response will be before running it.

## Database requirements
None — this project intentionally has no persistence.

## Models / Relationships / API requirements
Not applicable at this stage.

## Authentication / Validation requirements
None — out of scope for this project.

## Expected final result
A student can start the script, hit it from a browser and from `curl`
with different methods and paths, and correctly explain every part of
what they see in both directions.

## Difficulty
Low — the point is observation and understanding, not building
something complex.

## Estimated time
Fits within Week 2, Session 3 (one 3–4 hour session), building on
Sessions 1–2's conceptual groundwork.

## Prerequisite knowledge
Week 1's functions and control flow.

## Skills tested
Reading and explaining real HTTP traffic; branching logic based on
method and path.

## How to run it

```
python3 request_inspector.py
```

## How to test it manually

In another terminal:

```
curl -i "http://localhost:8000/hello?name=Eli"
curl -i -X POST -d '{"name": "test"}' http://localhost:8000/items
```

Confirm: the GET request's query parameters appear in the JSON response
and in the server's console log; the POST request's body is parsed and
echoed back; both return status `200`.

## Common errors

- `OSError: [Errno 98] Address already in use` — a previous instance is
  still running; stop it or change the `port` variable.
- A POST body showing as raw text instead of parsed JSON just means the
  client didn't send valid JSON — this is handled gracefully (see
  `_explain`), not treated as a crash.

## Complete code

See `request_inspector.py` in this folder.
