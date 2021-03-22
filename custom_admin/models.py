from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, null=True)
    category = models.ManyToManyField('Category')

    def __str__(self):
        return self.title

    # @property # create method and add its name to list_display 
    # def day_since_creation(self):
    #     diff=timezone.now() - self.date_created
    #     return 23


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Categories'
