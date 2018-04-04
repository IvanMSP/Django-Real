from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from empresa.models import Empresa



# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=250)
    empresa = models.OneToOneField(Empresa, related_name="empresas", blank=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (('draf', 'borrador'), ('published', 'publicado'))
    TAGS = (('D' , 'Deportes'), ('F', 'Finanzas'), ('C','Cultura'))
    title = models.CharField(max_length = 250)
    body = models.TextField()
    author = models.ForeignKey(User,related_name='blog_posts')
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)
    tag =models.CharField(choices= TAGS , max_length= 2,default='D', db_index=True)
    status = models.CharField(choices=STATUS_CHOICES,default='draf',max_length=10)
    blog = models.ManyToManyField(Blog, related_name='blog')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey(Post , related_name = "comments")
    body = models.TextField()
    user = models.ForeignKey(User,related_name='blog_comments', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Comentado por {}'. format(self.user,self.post)


