from django.urls import path

from books.views import BooksMainPageView, AllBooksView, BookDetailView, AuthorBooksView

urlpatterns = [
    path('', BooksMainPageView.as_view(), name='books_index'),
    path('books/', AllBooksView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('author/books/<int:pk>/', AuthorBooksView.as_view(), name='author_books'),

]