from django.contrib import admin
from book.models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate')
    list_display_links = ('name', 'birthdate')
    search_fields = ('name', 'birthdate')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'author')
    list_display_links = ('title', 'isbn', 'author')
    search_fields = ('title', 'isbn', 'author')
