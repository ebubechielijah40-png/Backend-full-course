from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html", {"name": "Eli"})


def about(request):
    bio = "I'm a backend developer building projects with Python and Django."
    return render(request, "pages/about.html", {"bio": bio})


def contact(request):
    return render(request, "pages/contact.html", {"email": "eli@example.com"})


def projects(request):
    project_list = [
        {"title": "Expense Tracker", "year": 2026},
        {"title": "Request Inspector", "year": 2026},
        {"title": "Personal Portfolio Site", "year": 2026},
    ]
    return render(request, "pages/projects.html", {"projects": project_list})
