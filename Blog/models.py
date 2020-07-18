from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    Description= models.CharField(max_length=200, blank=True, null= True)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):

    STATUS_CHOICES = (('Published', 'Published'),
                      ('Draft', 'Draft'),)
    title = models.TextField()
    subtitle = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255)
    status = models.CharField(max_length=10, default='Draft', choices= STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# one to many relation between post and category