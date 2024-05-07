from django.db import models
from django.urls import reverse

#1st class
class Content(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail_page", args=[str(self.pk)])
    
    