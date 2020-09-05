from django.urls import path
from .views import (
        # my_fbv,
        CourseView,
        CourseListView,
        CourseCreateView,
        CourseUpdateView,
        CourseDeleteView,
        MyListView
)
app_name = 'courses'
urlpatterns = [
    # path('',my_fbv, name='courses-list'),
    # in below the path rendering contact html page
    # path('', CourseView.as_view(template_name='contact.html'), name='course-view'),
    # there are same class view but rendering different templates
    path('', CourseListView.as_view(), name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    # path('', MyListView.as_view(), name='my-list'),
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name= 'courses-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
]