from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

    def __init__(self, *args, **kwargs):
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class ProfileCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ProfileCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})

    def clean_username(self):
        pass

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        if commit:
            user.save()
        return user

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


