from django.urls import path
from .views import register, login
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]