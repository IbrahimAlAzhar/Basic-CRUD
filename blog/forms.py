from django import forms
from .models import Article
# you can use either ArticleModelForm(modelForm based) or ArticleForm(Form based)


class ArticleModelForm(forms.ModelForm):
    # here title,content and active are build in from models.py,it will works by default

    class Meta:
        # if class meta remove then the class inherit from forms.Modelfrom to change to forms.Form
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]

'''
class ArticleForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Type the title"}))
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "your content",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 120
            }
        )
    )
    active = forms.BooleanField()
'''
