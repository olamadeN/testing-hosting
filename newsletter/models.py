from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    thumb = models.ImageField(default=None, upload_to="media/")
    date = models.DateTimeField(auto_now_add= True)
# this block of code is to show the title of the article in the admin page
    def __str__(self):
        return self.title

# this block of code is to create a snippet of the body so that the article-list will not show the whole body of the article
    def snapshot(self):
        return self.body[:360] + '...'

class Comment(models.Model):
    post = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE )
    name = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
# ensure to put this code when in the ORM but after making your migrations
# 'manage.py migrate --run-syncdb'