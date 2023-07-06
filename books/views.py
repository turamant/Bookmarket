from django.shortcuts import render, get_object_or_404
from django.views import View

from books.models import Book, Author, Category


# Create your views here.

class BooksMainPageView(View):
    def get(self, request):
        return render(request, "books/index.html")


class AllBooksView(View):
    def get(self, request):
        context = dict()
        books = Book.objects.all()
        context["books"] = books
        return render(request, "books/books_list.html", context)


class BookDetailView(View):
    def get(self, request, pk):
        context = dict()
        book = Book.objects.select_related('categories').get(id=pk)
        images = book.images_set.all()
        authors = book.authors.all()
        context["book"] = book
        context["authors"] = authors
        context["images"] = images
        return render(request, "books/book_detail.html", context)


class AuthorBooksView(View):
    def get(self, request, pk):
        context = dict()
        authors = Author.objects.prefetch_related('book_set').get(id=pk)
        books = authors.book_set.all()
        context["authors"] = authors
        context["books"] = books
        return render(request, "books/author_books.html", context)


class AllCategoryView(View):
    def get(self, request):
        context = dict()
        categories = Category.objects.all()
        context["categories"] = categories
        return render(request, "books/categories.html", context)


class CategoryBooksDetailView(View):
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        books = category.book_set.all()
        context = {"books": books, "category": category}
        return render(request, "books/category_books.html", context)
