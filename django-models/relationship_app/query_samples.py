from .models import Author, Book, Library, Librarian
from django.shortcuts import render

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books
    

def all_books_in_a_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    books.all()
    return books
    

def library_librarian(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

