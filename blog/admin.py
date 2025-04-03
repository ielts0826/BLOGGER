from django.contrib import admin
from .models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    list_filter = ('author', 'category', 'tags', 'created_at')
    search_fields = ('title', 'content')
    # ManyToManyField 不能直接在 list_display 显示，可以在这里添加一个方法
    # 或者直接在后台编辑页面管理

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
