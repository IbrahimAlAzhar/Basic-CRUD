from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)
app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    # if i use id instead of using pk then django shows Attribute Error
    # you can't use slug,you have to us id,title,content as a slug,if u use id then you have to use get method
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]