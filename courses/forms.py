from django import forms
from .models import Courses
# you can use either ArticleModelForm(modelForm based) or ArticleForm(Form based)


class CoursesModelForm(forms.ModelForm):
    # it inherit from ModelForm for that reason using Meta class and fields are just added
    # here title,content and active are build in from models.py,it will works by default

    class Meta:
        # if class meta remove then the class inherit from forms.Modelfrom to change to forms.Form
        model = Courses
        fields = [
            'title',
            'description',
        ]

    def clean_title(self):
        # Raw validation on a post method
        # define the function clean<field_name>
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError("This is not a valid title")
        return title
