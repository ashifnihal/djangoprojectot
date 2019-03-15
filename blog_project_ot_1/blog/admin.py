from django.contrib import admin
from blog.models import Post,CommentModel

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author','created','publish')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','body','created','updated','active')
    list_filter=('created','active')
    search_fields=('name','body')

admin.site.register(Post,PostAdmin)
admin.site.register(CommentModel,CommentAdmin)
