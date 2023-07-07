from books.models import Book


def last_books(request):
    books = Book.objects.order_by('-year')[:10]
    return {
        'last_books': books
    }