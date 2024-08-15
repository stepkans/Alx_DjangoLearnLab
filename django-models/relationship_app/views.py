from django.shortcuts import render
from .models import Author, Book, Library, Librarian

# Create your views here.
def books_list(request):
    book_list = Book.objects.all()

    context = {
        'book_list': book_list,
    }
    return render(request, 'relationship_app/list_books.html', context)

class BooksInLibrary(ListView):
    model = Library
    model = Book

    template_name = 'relationship_app/books_in_library.html'
    