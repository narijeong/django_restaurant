from django.contrib import admin
from .models import Post, Category, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author']
    search = ['title', 'author', 'content']


# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)