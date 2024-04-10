from django.urls import path
from profiles.views import (CreateProfileView, SingUp,
                            HomeView, logout_view, ProfileJson, ProfileView,
                            UpdateVisitor, DeleteProfileView, ApiVisitors,
                            AllVisitors)

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='register'),
    path('login/', SingUp.as_view(), name='login'),
    path('', HomeView.as_view(), name='home'),
    path('logout/', logout_view, name='logout'),
    path('profile_api/', ProfileJson.as_view(), name='profile_api'),
    path('users/', ProfileView.as_view(), name='users'),
    path('update_user/<int:profile_id>/', UpdateVisitor.as_view(), name='update_user'),
    path('delete_user/<int:profile_id>/', DeleteProfileView.as_view(), name='delete_user'),
    path('all_visitors_api/', ApiVisitors.as_view(), name='all_visitors_api'),
    path('all_visitors/', AllVisitors.as_view(), name='all_visitors'),

]
