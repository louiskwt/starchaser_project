from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


class AvailableNotesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="publihsed").filter(status="free")


# Create your models here.
class Note(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    TYPE_CHOICES = (
        ('free', 'Free'),
        ('paid', 'Paid'),
    )
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=256, unique_for_date='published_at')
    description = models.TextField(max_length=156)
    body = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    notes_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="free")
    available_notes = AvailableNotesManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('notes:note_detail', args=[self.published_at.year, self.published_at.month, self.published_at.day, self.slug])
    
    class Meta:
        ordering = ('-published_at',)
    
    def __str__(self):
        return self.title

