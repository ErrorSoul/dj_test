# coding: utf-8

from django.contrib import admin
from blog.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display=("title", "created", "tags")

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
