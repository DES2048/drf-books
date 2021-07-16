from django.urls import path
from books.views import author_list, book_list_view, book_detail_view


urlpatterns = [
    path("authors/", author_list, name="authors"),
    path("books/", book_list_view, name="books"),
    path("books/<int:pk>", book_detail_view, name="book-detail")
]
