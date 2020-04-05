from django.db import models
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model) : 

    name = models.CharField(max_length=128 , blank=False , unique=True)
    slug = models.SlugField(max_length=128 , blank=False , unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Article(models.Model) :

    title = models.CharField(max_length=128 , blank=False , unique=True , error_messages={"unique":"This title already exists..."})
    slug = models.SlugField(max_length=128 , blank=False , unique=True, error_messages={"unique":"This slug already exists..."})
    content = models.TextField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag , blank=True)

    def __str__(self):
        return self.title



