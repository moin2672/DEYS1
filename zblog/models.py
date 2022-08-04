from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        # return reverse('detail', args=(str(self.id)))
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=600)
    title_tag = models.CharField(max_length=600) #,default="DEYS RAVEZ!"
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body=models.TextField()
    body = RichTextField(blank=True, null=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('detail', args=(self.pk, ))
        # return reverse('detail', args=[self.pk]) # working
        # return reverse('detail', args=(str(self.pk)))
        # return reverse('home')

