from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article
from .forms import ArticleModelForm

# all are class based view


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm # here use this form and later check this validity in function
    queryset = Article.objects.all()
    # success_url = '/' # this is a another process to redirect the url after fill up the form

    def form_valid(self, form):
        # this method using for validation which one we use products/forms file
        print(form.cleaned_data) # print the data
        return super().form_valid(form) # return super class

    # def get_success_url(self):
     #   return '/'


class ArticleUpdateView(UpdateView):
    # after updated the model is rendered to get_absoulate_url method which render to detail html page
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        # for getting the id instead using pk in url
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleListView(ListView):
    # inherit from ListView, here creates a build in object list
    # it renders the template blog/modelname_list.html
    # one way to render the template, override this templates
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    # if i erase the template name then django shows Template does not exist
    # another way to define template is through the url.py
    template_name = 'articles/article_detail.html'
    # when u use get_object method then u no need to using queryset
    #queryset = Article.objects.all()
    # queryset = Article.objects.filter(id__gt=1) # it means which id is greater then 1 take it,then u no nee to this get
    # _object method, and use pk in url

    def get_object(self):
        # built in this method use because of using id instead of pk
        # this method directly can't call,the class automatically take it
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    # queryset = Articles.objects.all() # you can remove queryset because there the get_object method are called
    # success_url = '/articles/' # another process to redirect

    def get_object(self):
        # to catch a single id(object)
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        # using this method because after deleting the post the model's get absoulate url method does not exist
        # for this reason we have to use this model to redirect after delete a post
        return reverse('articles:article-list')
