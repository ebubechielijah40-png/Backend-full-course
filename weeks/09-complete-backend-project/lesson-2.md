# Lesson 2 — Building Models, ORM, and API Together

With a plan from Lesson 1, build in the same order the whole course has
used: models and migrations first (Weeks 4/6), then serializers and
endpoints (Week 7). No new concepts — this is applying Weeks 3–7 to a
new domain with reduced guidance.

**Guided activity:** Confirm your `Task` and `Category` models match
your Lesson 1 plan, migrate them, and register them with the admin
before writing any API code — this gives you a way to inspect your data
as you build, exactly as Week 4 taught.

**Task:** Build full CRUD endpoints for both `Category` and `Task`,
including the filtering by category and completion status the spec
requires (a `QuerySet.filter()` call on query parameters, same pattern
as Week 7's author filter).

**Debugging activity:** If your `Task` list endpoint returns a `500`
error mentioning `category_id`, check whether your serializer references
a field name that doesn't match your model's actual field — a mismatch
between model and serializer field names is one of the most common
integration bugs at this stage.

## Checkpoint

What determines the order you should build things in — models, then
serializers, then endpoints? (Each layer depends on the one before it:
you can't serialize a model that doesn't exist yet, and you can't build
an endpoint around a serializer that doesn't exist yet.)
