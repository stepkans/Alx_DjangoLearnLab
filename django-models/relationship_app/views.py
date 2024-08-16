from django.shortcuts import render
from .models import Library
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from .forms import BookForm 

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
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_books')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials.'}) 
        
    else:
        return render(request, 'relationship_app/login.html')    



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
    return render(request, 'relationship_app/register.html', context)

# Below are Helper functions to check user roles

def is_admin(user):
    """ Checks if user is an admin"""
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    """ Checks if user is a Librarian"""
    return user.userprofile.role == 'Librarian'

def is_member(user):
    """ Checks if user is a member"""
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
            
    else:
        form = BookForm()

    context = {
        'form': form
        }    
    return render(request, 'relationship_app/add_book.html', context)           


@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid:
            form.save()
            return redirect(request, 'books')
        
    else:
        form = BookForm(instance=book)

    context = {
        'form': form
        }    
    return render(request, 'relationship_app/edit_book.html', context)   

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    
    context = {
        'book': book
        }    
    return render(request, 'relationship_app/edit_book.html', context) 



