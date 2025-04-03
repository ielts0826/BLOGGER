from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'content')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'post__title', 'author__username')
