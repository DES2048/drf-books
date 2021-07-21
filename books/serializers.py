from rest_framework import serializers
from books.models import Author, Book, Tag


class NestedAuthorSerializer(serializers.ModelSerializer):
    ' represents authors in book list and book detail views'
    id = serializers.IntegerField(label="ID")
    name = serializers.CharField(max_length=128, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name"]


class NestedTagSerializer(serializers.ModelSerializer):
    ' represents authors in book list and book detail views'
    id = serializers.IntegerField(label="ID")
    title = serializers.CharField(max_length=128, read_only=True)

    class Meta:
        model = Tag
        fields = ["id", "title"]


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"


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


class BookDetailSerializer(serializers.ModelSerializer):
    authors = NestedAuthorSerializer(many=True)
    tags = NestedTagSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    ' for create/update/delete views'
    class Meta:
        model = Book
        fields = "__all__"
        extra_kwargs = {"tags": {"allow_empty": True}}
