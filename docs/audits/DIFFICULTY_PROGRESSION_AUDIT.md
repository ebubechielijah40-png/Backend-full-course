# Difficulty Progression Audit

This audit checks that the course rises in difficulty smoothly, and that
each week reuses — rather than discards — earlier knowledge.

## Target progression

```
Beginner
  → Basic programmer            (Week 1)
  → Beginner backend developer  (Weeks 2–4)
  → Database-aware backend dev  (Weeks 5–6)
  → API developer               (Weeks 7–8)
  → Independent backend dev     (Weeks 9–12)
```

## Step-by-step check

- **Week 1 → 2:** Week 1 ends with a student who can write organized
  Python and persist data to a file. Week 2 does not require new syntax
  knowledge — it reframes "a program that processes input" (already
  known) as "a program that processes an HTTP request" (new context, old
  skill). No difficulty spike.

- **Week 2 → 3:** Django's URL routing and views are, at this stage,
  "a function that takes a request and returns a response" — exactly the
  mental model built in Week 2, now inside a framework. No difficulty
  spike, because HTTP fluency (Week 2) is a direct prerequisite Django
  assumes.

- **Week 3 → 4:** Adding models to an already-familiar Django project is
  additive, not a restart. Migrations are new, but only one new idea is
  introduced at a time (models, then admin, then rendering) across the
  week's three sessions.

- **Week 4 → 5:** This is the one deliberate step *outside* Django, to
  make sure students understand relational data independent of any ORM
  "magic." This is a lateral move in context, not an increase in
  difficulty — SQL syntax is more explicit and arguably simpler than the
  Django admin students just used.

- **Week 5 → 6:** Direct reuse: the exact schema designed in SQL (Week 5)
  is rebuilt as Django models and queried with the ORM. This is the
  clearest reuse point in the course — SQL is connected to Django ORM
  exactly as required.

- **Week 6 → 7:** The Library Catalog application (already modeled and
  ORM-backed) becomes the same application's API. No new domain to learn
  — HTTP (Week 2) is connected to REST APIs (Week 7) via a project the
  student already understands end to end.

- **Week 7 → 8:** Authentication is added to an API students already
  built. This is additive complexity on a known base, not a new project.

- **Week 8 → 9:** No new syntax at all — Week 9 is explicitly an
  integration week. This is the course's intended "consolidation" step
  before the difficulty curve resumes climbing.

- **Week 9 → 10:** Testing is applied to the Week 9 backend, not to a new
  one. Reuses the exact application; adds one new skill (testing) at a
  time.

- **Week 10 → 11:** Deployment ships the exact same, now-tested backend.
  Reuses the application a third time. Git/GitHub, used informally since
  Week 1, is formalized here rather than introduced from zero.

- **Week 11 → 12:** The capstone requires everything above, applied to a
  new problem, independently. This is the single largest jump in the
  course by design — it is a demonstration of independence, not a new
  concept, and every underlying skill it requires was already
  individually demonstrated across Weeks 1–11.

## Reuse check (explicit dependencies named in the design brief)

| Requirement | Where it happens |
|---|---|
| Python reused in Django | Week 3 onward — all Django code is Python |
| SQL connected to Django ORM | Week 5 → Week 6, same schema rebuilt |
| HTTP connected to REST APIs | Week 2 → Week 7, same request/response model |
| Authentication added to the API | Week 7 → Week 8, same API |
| API becomes foundation of the larger backend | Week 8 → Week 9 |
| Testing applied to the existing backend | Week 9 → Week 10, same project |
| Deployment deploys the existing backend | Week 10 → Week 11, same project |
| Capstone requires everything previously learned | Week 12 |

## Conclusion

No sudden jump from beginner to advanced material was found. The single
intentionally large step is Week 11 → 12, which is appropriate because it
tests independence rather than introducing new material, and it is
prepared for across the preceding eleven weeks rather than sprung on
students unannounced.
