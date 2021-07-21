from django.urls import path
from books.views import (
    author_list, book_list_view, book_detail_view, tag_list_view,
    tag_detail_view
)

urlpatterns = [
    path("authors/", author_list, name="authors"),
    path("books/", book_list_view, name="books"),
    path("books/<int:pk>", book_detail_view, name="book-detail"),
    path("tags/", tag_list_view, name="tags"),
    path("tags/<int:pk>", tag_detail_view, name="tag-detail")
]
