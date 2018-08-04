from django.urls import path
from account.views import UserProfile, SignUpUser, EditProfile

urlpatterns = [
    path('signup/', SignUpUser.as_view(), name='signup'),
    path('profile/<str:slug>/', UserProfile.as_view(), name='profile'),
    path('edit/', EditProfile.as_view(), name='edit-profile')
]