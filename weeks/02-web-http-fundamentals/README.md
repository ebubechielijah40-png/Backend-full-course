# Week 2 — Web and HTTP Fundamentals

## What students already know

Organized Python: functions, control flow, error handling, file I/O and
JSON (Week 1). No web or networking knowledge yet.

## What they need to learn this week

- What a client and a server are, and what a request/response cycle is.
- HTTP methods (GET, POST, PUT/PATCH, DELETE) and when to use each.
- Status codes and what they communicate.
- The structure of a request and a response: method, path, headers, body.
- How to serve a basic dynamic response from Python and inspect real
  HTTP traffic.

## What they will build

A **Request Inspector** — a small Python script (using the standard
library's HTTP server) that receives requests, logs their method, path,
headers, and body, and returns a response explaining what it received.

## Concepts necessary to build it

Functions and control flow from Week 1 (to branch on method/path) and
file/print-based logging (also Week 1) — no new prerequisite beyond
what Week 1 already covers, plus this week's new HTTP concepts.

## What should NOT be taught yet

- Django or any web framework (Week 3).
- Building a multi-threaded or production-grade server — a single
  request at a time is enough to demonstrate the concepts.
- REST API design conventions (Week 7) — this week is about understanding
  raw HTTP, not designing a good API.

## What the three sessions accomplish

1. **How the web works** — client/server model, a plain-English request/
   response walkthrough, first look at browser dev tools.
2. **HTTP in detail** — methods, status codes, headers, query strings vs.
   request bodies, hands-on with a CLI HTTP client.
3. **Serving dynamic content** — building the Request Inspector and
   testing it against real requests from a browser and a CLI tool.

## What the project accomplishes

Turns HTTP from an abstract idea into something the student has watched
happen, byte by byte, and can explain in their own words.

## Practical skill at week's end

Can read any HTTP request or response and explain what each part means;
understands, concretely, what a web framework like Django will be doing
for them starting next week.

---

**Status:** blueprint and project specification complete. Detailed
lesson content (`lesson-1.md`, `lesson-2.md`, `lesson-3.md`) has not yet
been written — see `../../docs/audits/WORKLOAD_AUDIT.md` and
`../../docs/audits/DIFFICULTY_PROGRESSION_AUDIT.md` for how this week was
scoped before lesson writing begins.
