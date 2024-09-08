from rest_framework import serializers
from .models import Author, Book
import datetime
class BookSerializer(serializers.ModelSerializer):
    """
        The Book model represents a book.
        It has these fields 'title', 'publication_year', and a foreign key to the Author model.
    """
    class Meta:
        model = Book
        fields = "__all__"
        
    # Custom validation for publication_year
    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value    
        
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    """
        The Author model represents a book author.
        It contains just a 'name' field for the author's name.
    """
    class Meta:
        model = Author
        fields = ('name',)
