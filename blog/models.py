from django.db import models
from django.contrib.auth.models import User




class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    pic = models.ImageField(upload_to='images/')
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField('Tag')
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    tag_name = models.CharField(max_length=256)