# Lesson 2 — HTTP in Detail

## Methods

- **GET** — retrieve data, no side effects. Use for "show me X."
- **POST** — create something new. Use for "add X."
- **PUT/PATCH** — update something existing (`PUT` replaces the whole
  thing, `PATCH` updates part of it).
- **DELETE** — remove something.

This matters because choosing the right method is how a server (and
anyone reading your API later, including you in six months) knows what
an endpoint is supposed to do without reading its code.

**Task:** For each of these actions, name the HTTP method you'd expect:
"view a list of expenses," "add a new expense," "change an expense's
category," "remove an expense." (GET, POST, PATCH, DELETE.)

## Status codes

Grouped by first digit:

- **2xx** — success (`200 OK`, `201 Created`).
- **3xx** — redirect.
- **4xx** — client's fault (`400 Bad Request`, `404 Not Found`).
- **5xx** — server's fault (`500 Internal Server Error`).

**Common error (conceptual):** returning `200 OK` for a failed operation
(e.g. "user not found" with a `200` and an error message in the body)
makes it impossible for a client to detect failure without parsing the
body — always match the status code to what actually happened.

## Headers, query strings, and bodies

**Headers** carry metadata (`Content-Type: application/json` tells the
receiver how to interpret the body). A **query string**
(`?category=Food`) passes small amounts of data in the URL itself,
usually for GET requests. A **body** carries larger or structured data,
usually for POST/PUT/PATCH.

**Guided activity:** Using a CLI HTTP client, install/confirm `curl` is
available, then run:

```
curl -i https://httpbin.org/get?category=Food
```

Identify the status code, at least one header, and the echoed query
string in the response body.

**Debugging activity:** This description of an endpoint is wrong — find
the mistake: "To delete a resource, send a GET request to `/items/5/
delete`." (The bug: deletion should use the `DELETE` method on
`/items/5/`, not a GET request to a special delete path — GET requests
should never have side effects like deleting data.)

## Checkpoint

Which status code range means "the client sent something wrong," and
which means "the server itself failed"? (4xx; 5xx.)

## Independent challenge

Using `curl -i`, send a GET request to `https://httpbin.org/status/404`
and to `https://httpbin.org/status/500`. Confirm the status codes match
what the URL asked for, and explain in one sentence what each code
category means.
