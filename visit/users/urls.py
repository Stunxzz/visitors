from django.urls import path
from .views import LoginView,visit
urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("visitor/",visit, name="visitor")

]