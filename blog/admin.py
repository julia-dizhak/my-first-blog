from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'approved_comment')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
