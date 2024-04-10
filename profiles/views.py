from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView
from .models import Profile
from .forms import ProfileCreationForm, EmailAuthenticationForm
from django.contrib.auth.views import LoginView


class SingUp(LoginView):
    template_name = 'login.html'
    form_class = EmailAuthenticationForm
    success_url = reverse_lazy('visitors')

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('users')
        else:
            return reverse_lazy('visitors')


class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'register.html'

    def form_valid(self, form):
        profile = form.save()
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


class ProfileJson(View):
    def get(self, request, *args, **kwargs):
        profiles = Profile.objects.all()
        json_profiles = []
        for profile in profiles:
            json_info = {
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'email': profile.email,
                'admin': profile.is_staff
            }
            json_profiles.append(json_info)
        return JsonResponse(json_profiles, safe=False)


class ProfileView(TemplateView):
    template_name = 'users_dashboard.html'