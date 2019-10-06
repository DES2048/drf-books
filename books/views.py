from rest_framework import generics
from rest_framework import filters
from books.models import Author, Book
from books.serializers import (
    AuthorSerializer, BookFromSerializer, BookToSerializer)


class MethodSerializerMixin:

    def get_serializer_class(self):

        method = self.request.method

        if hasattr(self, 'method_serializers'):
            serializer_class = self.method_serializers.get(
                method,
                super().get_serializer_class()
            )
        else:
            serializer_class = super().get_serializer_class()

        return serializer_class


class AuthorsList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class BookList(MethodSerializerMixin, generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookFromSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    method_serializers = {
        'POST': BookToSerializer,
    }


class BookDetailView(MethodSerializerMixin, generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookFromSerializer

    method_serializers = {
        'PUT': BookToSerializer,
        'PATCH': BookToSerializer,
    }


class AuthorDetail(generics.RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
