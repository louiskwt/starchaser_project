from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('private', 'Private'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=256, unique_for_date='publish')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published_posts = PublishedPostManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
    
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

