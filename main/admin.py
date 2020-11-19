from django.contrib import admin
from .models import Category, News, Comment, Search

admin.site.register(Category)
admin.site.register(Search)

class AdminNews(admin.ModelAdmin):

    list_display=('title', 'category', 'add_time')

admin.site.register(News, AdminNews)


class AdminComment(admin.ModelAdmin):
    list_display = ('news', 'email', 'comment', 'status')
admin.site.register(Comment, AdminComment)

