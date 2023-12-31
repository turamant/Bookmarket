import os
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from books.models import Book, Author, Category


# Create your views here.

class BooksMainPageView(View):
    def get(self, request):
        return render(request, "books/index.html")


class AllBooksView(View):
    def get(self, request):
        paginator = Paginator(Book.objects.filter(is_visible=True), per_page=2)
        page = paginator.page(request.GET.get('page', 1))
        context = dict()
        # books = Book.objects.all()
        context["books"] = page.object_list
        context["page_obj"] = page
        return render(request, "books/books_list.html", context)


class AllAuthorsView(View):
    template_name = "books/authors_list.html"
    context = dict()

    def get(self, request):
        authors = Author.objects.all()
        self.context["authors"] = authors
        return render(request, self.template_name, self.context)


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


def download_pdf(request):
    file_path = os.path.join(settings.MEDIA_ROOT)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response


class SearchResultsView(ListView):
    model = Book
    template_name = 'books/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Book.objects.filter(Q(title__iregex=query)
                                          | Q(authors__last_name__icontains=query)
                                          | Q(authors__first_name__icontains=query))
        return object_list


def category(request, pk):
    category = get_object_or_404(Category, id=pk)

    return render(request, 'books/category.html', {'category': category})
