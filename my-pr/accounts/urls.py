from django.urls import path
from .views import SignUp, ProfileView, EditProfileView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/<pk>/edit/', EditProfileView.as_view(), name='edit'),
    path('profile/<pk>/', ProfileView.as_view(), name='profile'),
]