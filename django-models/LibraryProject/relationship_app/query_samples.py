from .models import Author, Book, Library, Librarian
from django.shortcuts import render

# Prepare a Python script query_samples.py in the relationship_app directory. 
# This script should contain the query for each of the following of relationship:
# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.


def books_by_author(request, author):
    books_by_author = Book.objects.filter(author=author)
    context = {
        'books_by_author': books_by_author ,
    }
    return render (request, context, 'relationship_app/books_by_author.html')
def all_books(request):
    all_books = Book.objects.all()
    context = {
        "all_books" : all_books,
    }
    return render (request, context, 'relationship_app/all_books.html')

def librarians(request):
    librarian = Library.objects.get(librarian)
    
    context = {
        "librarian" : librarian,
    }
    return render (request, context, 'relationship_app/librarian.html')

