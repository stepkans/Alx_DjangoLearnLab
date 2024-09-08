"""_summary_
"""
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from .serializers import BookSerializer


from .models import Book
# Create your views here.

class BookListAPIView(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticated]