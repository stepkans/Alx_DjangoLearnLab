from rest_framework import serializers
from .models import Author, Book
import datetime

class AuthorSerializer(serializers.ModelSerializer):
    """
        The Author model represents a book author.
        It contains just a 'name' field for the author's name.
    """
    class Meta:
        model = Author
        fields = ('name',)

class BookSerializer(serializers.ModelSerializer):
    """
        The Book model represents a book.
        It has these fields 'title', 'publication_year', and a foreign key to the Author model.
    """
    class Meta:
        model = Book
        fields = "__all__"
        
        