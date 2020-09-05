from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120)
    # blank true means this box can be empty,you can just ignore it,null means database can null or empty
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=False,null=False)
    featured = models.BooleanField(default=True) # null= True, default = True

    def get_absolute_url(self):
        # here azhar is app name in url, and product-detail is url name of product detail
        return reverse("azhar:product-detail", kwargs={"my_id": self.id})
