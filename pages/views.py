from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def home_view(request,*args, **kwargs):
    print(args, kwargs)
    print(request)
    print(request.user)
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request,"products/home.html", {})


def contact_view(request,*args, **kwargs):
    # return HttpResponse("<h1>Contact page</h1>")
    return render(request, "products/contact.html", {})


def about_view(request,*args, **kwargs):
    print(request.user)
    # return HttpResponse("<h1>Hello from the other side</h1>")
    my_context = {
        "my_text": "this is about us",
        "my_name": "ibrahim al azhar",
        "my_number": 123,
        "my_list": [12,23,23,44,"abc","azhar"],
        "my_html": "<h1>This one is html tag</h1>"
    }
    return render(request, "products/about.html", my_context)


def social_view(request,*args, **kwargs):
    # return HttpResponse("<h1>Social page</h1>")
    return render(request, "products/social.html", {})