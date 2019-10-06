from rest_framework import serializers
from books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookFromSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookToSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
