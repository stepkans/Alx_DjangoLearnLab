from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserManager(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username' ,'date_of_birth','is_staff')

admin.site.register(CustomUser,CustomUserManager)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book,BookAdmin)
