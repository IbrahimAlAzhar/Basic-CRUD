from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm, RawProductForm


def product_create_view(request):
    form = ProductForm(request.POST or None) # if the method is post method or other method then show the form and save it
    if form.is_valid():  # if the form is valid,then save the form and then show a empty form
        form.save()
        form = ProductForm() # for get method
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)


def product_update_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id) # detect one id
    form = ProductForm(request.POST or None, instance=obj) # create a instance of class ProductForm
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_list_view(request):
    queryset = Product.objects.all() # to gather all id
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def product_detail_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    # POST request
    if request.method == "POST":
        # confirming the deleting
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    # in below this line means when some id are not in database then it render page not found instead of DoesNotExist
    obj = get_object_or_404(Product, id=my_id) # get_object_or_404 takes the object or shows page not found
    # obj.delete()

    # obj = Product.objects.get(id=my_id) # if this line is un comment then shows 'Does not exist'
    # try:
    #  obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #   raise Http404
    context = {
       "object": obj
    }
    return render(request, "products/product_detail.html", context)


def render_initial_data(request):
    # the two product_create_view methods are same,first one acting shortcut
    initial_data = {
        'title': "My this awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)




'''
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_create_view(request):
    my_form = RawProductForm() # creating a instance of a class RawProductForm
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            # now the data is good
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data) # here put in ** so that save in database
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html",context)

'''

def product_create_form(request):
    # print(request.GET)
    # print(request.POST)
    # for this condition here does'nt print None
    if request.method == 'POST':
        my_new_title = request.POST.get('title')
        print(my_new_title)
    context = {}
    return render(request, "products/product_create.html",context)




'''
def product_create_form(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm() # re render the form,for that reason after fill up this form then it will be empty
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    'title': obj.title,
    'description': obj.description,
    'price': obj.price,
    'summary': obj.summary

    context = {
       'object': obj
    }
    return render(request,"products/product_detail.html", context)
'''


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
