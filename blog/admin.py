from django.contrib import admin
from .models import Post, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_vlue_display = '-empty-'
    list_display = ('title','author', 'counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status','author',)
    ordering = ['created_date']
    search_fields= ['title', 'content']
admin.site.register(Post,PostAdmin)    
admin.site.register(Category)