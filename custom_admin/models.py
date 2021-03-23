from django.core.validators import validate_slug, validate_email
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, null=True, validators=[validate_slug])
    email = models.EmailField(null=True, validators=[validate_email])
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
    photo = models.ImageField(blank=True, null=True, upload_to='photos/%y/%m')
    active_name = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.blog.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Categories'
