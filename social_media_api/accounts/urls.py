from django.urls import path
from .views import register, login
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('users/<int:user_id>/follow/', FollowUserView.as_view(), name='follow-user'),
    path('users/<int:user_id>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
]