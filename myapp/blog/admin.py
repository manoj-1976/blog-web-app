from django.contrib import admin
from .models import Post,Category,AboutUS


class PostAdmin(admin.ModelAdmin):
    search_fields =('title','content')
    list_filter = ('category', 'created_at')

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(AboutUS)