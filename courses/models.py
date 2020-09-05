from django.db import models
from django.urls import reverse


class Courses(models.Model):
    title = models.CharField(max_length=120)
    # blank true means this box can be empty,you can just ignore it,null means database can null or empty
    description = models.TextField(blank=True, null=True)




