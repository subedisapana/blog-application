from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    STATUS_CHOICES = (('Published', 'Published'),
                      ('Draft', 'Draft'),)
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)
    status = models.CharField(max_length=10, default='Draft', choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
