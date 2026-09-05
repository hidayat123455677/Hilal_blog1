from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish_date', 'status')
    list_filter = ('status', 'publish_date', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}