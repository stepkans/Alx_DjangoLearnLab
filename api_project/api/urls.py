from django.urls import path, include
from rest_framework import routers
from .views import BookListAPIView

router = routers.DefaultRouter()
router.register(r'books', BookListAPIView)


urlpatterns = [
    path('book/', BookListAPIView.as_view(), name='book-list'),
]
