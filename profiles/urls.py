from django.urls import path
from profiles.views import CreateProfileView, SingUp, HomeView, logout_view

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='register'),
    path('login/', SingUp.as_view(), name='login'),
    path('', HomeView.as_view(), name='home'),
    path('logout/', logout_view, name='logout'),

]
