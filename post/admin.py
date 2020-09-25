from django.contrib import admin
from .models import Post,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=["title","publishing_date","user","slug"]
    list_display_links=["publishing_date"]
    list_filter = ["title", "content"]
    list_editable = ["title"]
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name","content","created_date"]
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)