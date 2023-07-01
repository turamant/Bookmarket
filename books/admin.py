from django.contrib import admin

from books.models import Author, Book, Images, Category

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Images)
admin.site.register(Category)



