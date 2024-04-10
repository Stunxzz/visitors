from django.urls import path
from profiles.views import (CreateProfileView, SingUp,
                            HomeView, logout_view, ProfileJson,ProfileView)

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='register'),
    path('login/', SingUp.as_view(), name='login'),
    path('', HomeView.as_view(), name='home'),
    path('logout/', logout_view, name='logout'),
    path('profile_api/', ProfileJson.as_view(), name='profile_api'),
    path('users/', ProfileView.as_view(), name='users'),

]
