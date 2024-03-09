from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.category_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, through='BlogTag')

    def __str__(self):
        return self.title

class BlogTag(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.blog.title} - {self.tag.tag_name}'



class Image(models.Model):
    blog = models.ForeignKey(Blog, related_name='images', on_delete=models.CASCADE)
    image_blob = models.ImageField(upload_to='blog_images')

    def __str__(self):
        return f'Image for {self.blog.title}'


    


