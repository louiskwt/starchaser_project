from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug', 'published_at', 'status', 'notes_type')
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
 