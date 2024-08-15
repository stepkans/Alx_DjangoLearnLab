from django.shortcuts import render
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.
def books_list(request):
    book_list = Book.objects.all()

    context = {
        'book_list': book_list,
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    