from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # when deleing autho, delete a post too (cascade delete)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name