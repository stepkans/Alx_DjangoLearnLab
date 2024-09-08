"""
Module providing a function printing python version.
"""
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """ 
    class Meta: 
        model = Book
        fields = "__all__"


