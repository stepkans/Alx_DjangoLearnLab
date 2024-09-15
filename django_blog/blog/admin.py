from django.contrib import admin
from .models import Post

# Register your models here.
# class PostAdmin(ModelAdmin):
#     list_display = 

admin.site.register(Post)
