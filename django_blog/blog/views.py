from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, PostForm, CommentForm
from django.urls import reverse_lazy
from .models import Post, Comment



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

# class LoginView(LoginView):
#     template_name = 'login.html'

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

class PostListView(ListView):
    model =  Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model =  Post
    template_name = 'blog/post_detail.html'
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html' 
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Ensuring only the author can update the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):          
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')

    # Ensure only the author can delete the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
@method_decorator(login_required, name='dispatch')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()  
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author    
    
    
def posts_by_tag():
    pass   

