from django.contrib import admin
from .models import Book


class Book_table(admin.ModelAdmin):
    list_display=('name','author','isbn','publisher')

# Register your models here.
admin.site.register(Book,Book_table)


