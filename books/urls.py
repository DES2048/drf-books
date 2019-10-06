from django.urls import path
from books.views import AuthorsList, BookList, BookDetailView


urlpatterns = [
    path("authors/", AuthorsList.as_view(), name="authors"),
    path("books/", BookList.as_view(), name="books"),
    path("books/<int:pk>", BookDetailView.as_view(), name="book-detail")
]