from django.contrib import admin
from django.contrib.auth.models import User
from web.models import  BlogPost

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated",)
    list_editable = ("published",)

admin.site.register(BlogPost, BlogPostAdmin)


