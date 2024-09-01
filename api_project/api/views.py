from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework import generics
from .models import Book
# Create your views here.

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  


