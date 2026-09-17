# Lesson 3 — Git/GitHub Workflow, Deploying, and Verifying

## A real commit history

Since Week 1, you've likely been using Git informally. This week,
formalize it: commit at meaningful points (not one giant "final commit"
at the end), with messages describing *what* changed and *why*:

```
git add .
git commit -m "Add environment-based settings for production"
git push
```

**Task:** Review your Task Manager's commit history. If it's a single
commit, that's a sign to work in smaller, more frequent commits from
here on — going forward, commit after each meaningful change (a working
feature, a passing test, a fixed bug), not only at the end of a session.

## Branching, briefly

For a solo project, a single `main` branch is fine. For any
collaborative work, create a branch per feature and merge it back:

```
git checkout -b add-search-endpoint
# ... make changes, commit ...
git checkout main
git merge add-search-endpoint
```

## Deploying and verifying

Follow `project/README.md`'s deployment steps for the chosen host, then
verify the live deployment the same way you verified it locally in
Week 9: hit the live URL with `curl`, confirm authentication and
ownership checks still work exactly as they did locally.

**Debugging activity:** A deployment succeeds but every request returns
a `500` error. What's the first thing to check? (The platform's deploy
logs — they almost always show the actual traceback, most commonly a
missing environment variable or an un-run migration.)

## Checkpoint

Why verify the *live* deployment the same way you verified the local
version, rather than assuming "it worked locally, so it's fine"?
(Because production configuration — environment variables, `DEBUG`,
`ALLOWED_HOSTS`, the real database — differs from local development, and
any of those can break something that worked locally.)

## Independent challenge

Complete the full Week 11 project (see `project/README.md`): hardened
settings, a real commit history, and a live, working deployment of the
Task Manager API.
