from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Courses
from .forms import CoursesModelForm
# all are Raw class based view not build in


class CourseObjectMixin(object):
    # Custom mixin for class based views,which is use for get_object
    model = Courses
    # inherit this class when need to find get_object, here this function is so those class which one needs this method
    # they inherit this class

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj


class CourseDeleteView(CourseObjectMixin, View): # here we inherit from custom mixin,there are lot of django build in mixin like login, inherit from simple class base view,not Generic Class Based View
    # inherit from CourseObjectMixin so don't need to write get_object method
    # Raw delete class based view,identical to Course update view,but there are no form here
    template_name = "courses/course_delete.html"

    def get(self, request, id=None, *args, **kwargs):
        # GET method(for find something )
        context = {}
        obj = self.get_object() # get_object function catch the id and take get_object_or_404,this method inherited
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self,request, id=None, *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None # for that reason the obj is deleted
            return redirect('/courses/') # that's imp thing after delete the redirect path
        return render(request, self.template_name, context)


class CourseUpdateView(CourseObjectMixin, View):
    # Raw update class based view
    template_name = "courses/course_update.html"

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object() # get_object function catch the id and take get_object_or_404
        if obj is not None:
            form = CoursesModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CoursesModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save() # form is save in POST method
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)


class CourseCreateView(View):
    # raw create class based view, This one doesn't need to get_object method,so it doesn't need to inheritance
    template_name = "courses/course_create.html"

    def get(self, request, *args, **kwargs):
        # GET method(it's using for searching and we find something on the url)
        form = CoursesModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method (post something in the form)
        form = CoursesModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CoursesModelForm() # this line is using for redirect the same page after fill up the form removing the title and description
        context = {"form": form}
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = Courses.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        # here the object_list passing to html page
        return render(request, self.template_name, context)


class MyListView(CourseListView):
    # inherit from CourseListView class to filter id=1,this is the biggest benefiet of class based view
    # which one is inherit property
    queryset = Courses.objects.filter(id=1)


class CourseView(CourseObjectMixin, View):
    # BASE VIEW Class = VIEW
    # this is function based view under the class based view
    template_name = "courses/course_detail.html"

    def get(self, request, id=None, *args, **kwargs):
        # new_obj = CourseView, to handle this type of obj so use self parameter
        # in the class view you have to set the default name of the function get,you can't use my_fbv as a method name
        # here using parameter self because handling the new obj of the class
        # GET method, This is raw Detail Class based view
        # this get_object method inherit from super class CourseObjectMixin
        context = {'object': self.get_object()}  # passing the object to detail template using context dictionary
        # this object use in course_detail.html file
        return render(request, self.template_name, context)

    '''def post(self, request, *args, **kwargs):
        # if you submitting a form then you have to use post method
        return render(request, 'about.html', {}) '''


def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, 'courses/about.html', {})
