from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','slug','status','publish')
    list_filter = ('status',)
    search_fields = ('title','body')
    date_hierarchy = 'publish'
    list_editable = ('status',)