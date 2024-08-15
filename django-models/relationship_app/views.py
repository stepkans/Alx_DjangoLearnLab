from django.shortcuts import render
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here. .
def books_list(request):
    book_list = Book.objects.all()

    context = {
        'book_list': book_list,
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')    
    else:
        form = UserCreationForm() 
    context = {
        'form': form,
    }    
    return render(request, 'relationship_app/library_detail.html', context)