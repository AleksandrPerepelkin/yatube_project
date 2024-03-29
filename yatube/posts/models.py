from email.headerregistry import Group
from tokenize import group
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )


class Group(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    
    def __srt__(self):
        return self.title