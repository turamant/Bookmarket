
from django.urls import path

from books.views import BooksMainPageView, AllBooksView, BookDetailView, AuthorBooksView, AllCategoryView, \
    CategoryBooksDetailView, download_pdf, AllAuthorsView

urlpatterns = [
    path('', AllBooksView.as_view(), name='books_list'),
    path('categories/', AllCategoryView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryBooksDetailView.as_view(), name='category_detail'),
    path('list/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('author/books/<int:pk>/', AuthorBooksView.as_view(), name='author_book'),
    path('authors/', AllAuthorsView.as_view(), name='authors_list'),
    path('download_pdf/', download_pdf, name='download_pdf'),

]
