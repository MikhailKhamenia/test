from django.contrib import admin
from .models import *
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'code', 'photo')
    list_display_links = ('id', 'title', 'code')

class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name')
    list_display_links = ('id', 'last_name', 'first_name')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class BorrowingAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'reader', 'date_taken', 'date_returned')
    list_display_links = ('id', 'book', 'reader', 'date_taken', 'date_returned')



admin.site.register(Book, BookAdmin)
admin.site.register(Reader, ReaderAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Borrowing, BorrowingAdmin)