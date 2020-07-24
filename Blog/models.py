from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50, null=False)
    host = models.CharField(max_length=50, null=False)
    port = models.CharField(max_length=5, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


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
    #publisher = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
