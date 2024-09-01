from django.urls import path, include
from rest_framework import routers
from .views import BookListAPIView
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [
    path('book-list/', BookListAPIView.as_view(), name='book-list'),
    path('api/', include(router.urls)),
]
