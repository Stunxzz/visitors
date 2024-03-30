from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .models import Profile
from .forms import ProfileCreationForm
from django.contrib.auth.views import LoginView, LogoutView


class SingUp(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('visitors')


class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'register.html'

    def form_valid(self, form):
        profile = form.save()
        print(profile.email)
        print(profile.password)
        user = authenticate(request=self.request, email=profile.email, password=form.cleaned_data['password1'])
        if user is not None:
            login(self.request, user)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('visitors')


class HomeView(TemplateView):
    template_name = 'home.html'


def logout_view(request):
    logout(request)
    return redirect('home')