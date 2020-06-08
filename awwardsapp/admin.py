from django.contrib import admin
from .models import Post
# Register your models here.

#customizing display of data
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'rating', 'location', 'slug', 'created_on', 'status', 'content')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)