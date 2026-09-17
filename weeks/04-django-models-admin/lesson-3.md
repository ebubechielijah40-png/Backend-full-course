# Lesson 3 — Rendering Model Data in Templates

## Querying models in a view

A view can fetch model instances directly from the database and pass
them to a template — no hardcoded list required:

```python
# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.order_by("-published_at")
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})
```

`Post.objects.order_by("-published_at")` fetches every post, newest
first (the `-` means descending). `get_object_or_404` fetches one post
by primary key, automatically returning a proper `404` response if it
doesn't exist, instead of crashing. This is your first real use of the
**ORM** — full depth comes in Week 6, but this is the same underlying
idea.

```html
<!-- blog/templates/blog/post_list.html -->
{% for post in posts %}
  <h2><a href="{% url 'post_detail' post.id %}">{{ post.title }}</a></h2>
  <p>By {{ post.author }} on {{ post.published_at }}</p>
{% endfor %}
```

**Debugging activity:** A student's post list page shows a
`NoReverseMatch` error mentioning `post_detail`. What are the two most
likely causes? (Either the URL pattern for `post_detail` doesn't exist
or isn't named `post_detail`, or it's missing its `<int:post_id>`
parameter that `{% url %}` needs to fill in.)

## Checkpoint

What does `get_object_or_404` do differently from a plain
`Post.objects.get(id=post_id)`? (It automatically returns a proper `404`
response if no matching row exists, instead of raising an unhandled
exception that would crash the view.)

## Independent challenge

Finish the blog (see `project/README.md`): a list page and a detail
page, both reading from the database, manageable entirely through the
Django admin with no hardcoded content.
