from rest_framework import serializers
from books.models import Author, Book


class NestedAuthorSerializer(serializers.ModelSerializer):
    ' represents authors in book list and book detail views'
    id = serializers.IntegerField(label="ID")
    name = serializers.CharField(max_length=128, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name"]


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"


class BookListSerializer(serializers.ModelSerializer):
    ''' used for list and detail view'''
    authors = NestedAuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    ' for create/update/delete views'
    class Meta:
        model = Book
        fields = "__all__"
