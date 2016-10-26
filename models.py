
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=50)
    image = models.FileField(upload_to="user_images")
    projects = models.TextField()

    def __unicode__(self):
        return self.user

class Project(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    image = models.FileField(upload_to="post_images")
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title + "-" +self.author

class Comment(models.Model):
    project = models.ForeignKey(Post)
    author = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.project + "-" +self.author