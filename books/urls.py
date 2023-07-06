
from django.urls import path

from books.views import BooksMainPageView, AllBooksView, BookDetailView, AuthorBooksView, AllCategoryView, \
    CategoryBooksDetailView, download_pdf, AllAuthorsView, SearchResultsView, category

urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('', AllBooksView.as_view(), name='books_list'),
    path('categories/', AllCategoryView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryBooksDetailView.as_view(), name='category_detail'),
    path('author/books/<int:pk>/', AuthorBooksView.as_view(), name='author_book'),
    path('authors/', AllAuthorsView.as_view(), name='authors_list'),
    path('download_pdf/', download_pdf, name='download_pdf'),
    path('category/<int:pk>/', category, name='category'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),


]
