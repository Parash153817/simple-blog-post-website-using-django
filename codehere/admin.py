
from django.contrib import admin
from .models import Note
# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'user', 'created_at', 'updated_at')

    list_filter = ('created_at', 'updated_at')

    search_fields = ('title', 'content', 'user__username')

    ordering = ('-created_at',)