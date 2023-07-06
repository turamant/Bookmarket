
from django.urls import path

from books.views import BooksMainPageView, AllBooksView, BookDetailView, AuthorBooksView, AllCategoryView, \
    CategoryBooksDetailView

urlpatterns = [
    path('', BooksMainPageView.as_view(), name='books_index'),
    path('list/', AllBooksView.as_view(), name='books_list'),
    path('categories/', AllCategoryView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryBooksDetailView.as_view(), name='category_detail'),
    path('list/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('author/books/<int:pk>/', AuthorBooksView.as_view(), name='author_books'),

]
