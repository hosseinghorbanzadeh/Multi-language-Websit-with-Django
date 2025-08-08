from django.contrib import admin
from blogpage.models import Post,Category,Comment

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy="created_date"
    empty_value_display = "-empty-"
    list_display = ["title", "counted_views","status", "published_date","author","login_require"]
    list_filter = ('status','author',)
    search_fields=['title','content']
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy="created_date"
    empty_value_display = "-empty-"
    list_display = ["name", "post","approve", "created_date"]
    list_filter = ('post','approve',)
    search_fields=['name','post ']
    summernote_fields = ('content',)

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)


