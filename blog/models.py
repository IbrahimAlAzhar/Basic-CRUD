from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    # this method is using where rendering when submit the form
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})