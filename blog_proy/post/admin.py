from django.contrib import admin

from .models import Post, Comments, Blog
from empresa.models import Empresa
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','body']
    list_filter = ['created','updated','title']
    search_fields = ['title','blog__empresa__name','author__user__username']
admin.site.register(Post, PostAdmin)
admin.site.register(Comments)
admin.site.register(Blog)