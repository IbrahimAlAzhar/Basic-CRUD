from django import forms
from .models import Product

# the form of ProductForm and RawProductForm acts same,deference is how view handles this


class ProductForm(forms.ModelForm):
    # here title,description and price are override,so there are no label,no email
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Type the title"}))
    email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 120
            }
        )
    )
    price = forms.DecimalField(initial=122)

    class Meta:
        # if class meta remove then the class inherit from forms.Modelfrom to change to forms.Form
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
     # here the title is override so there use args and kwargs
     # this method using for validation

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "modon" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Type the title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 120
            }
        )
    )
    price = forms.DecimalField(initial=122)
