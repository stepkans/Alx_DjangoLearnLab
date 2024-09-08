"""_summary_
    I HME MADE EFFO 
"""
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from django.urls import path, include
from .views import BookListAPIView
from .views import BookViewSet


router = routers.DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [
    path('book-list/', BookListAPIView.as_view(), name='book-list'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
