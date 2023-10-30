from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, mixins
from django.contrib.auth.backends import UserModel
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views import View, generic

from .helpers import LdapStatusCode, LdapUserAttributes

def visit(response):
    return render(response,"visitor.html")

class LoginView(auth_views.LoginView):
    _URL = r"http://10.57.1.43:8081/api/login"
    # TODO: Change _APP_NAME
    _APP_NAME = "visit"  # TODO трябва да се смени името на app
    template_name = "login.html"
    success_url = reverse_lazy("login")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy("visitor"))
        if request.POST:
            app_name = self._APP_NAME
            url = self._URL
            username = request.POST["username"]
            password = request.POST["password"]
            status = LdapStatusCode(app_name, url, username, password).get_status_code()
            if status == 200:
                user = LdapUserAttributes(app_name, url, username, password)
                username, first_name, last_name, personal_number, email = user.get_all_attributes()
                if username:
                    try:
                        login_user = UserModel.object.get(personal_number=personal_number)
                        first_name_condition = login_user.first_name == first_name
                        last_name_condition = login_user.last_name == last_name
                        username_condition = login_user.username == username
                        email_condition = login_user.email == email
                        if any([not first_name_condition,
                                not last_name_condition,
                                not username_condition,
                                not email_condition]):
                            login_user.first_name = first_name
                            login_user.last_name = last_name
                            login_user.username = username
                            login_user.email = email
                            login_user.save()
                    except UserModel.DoesNotExist:
                        login_user = UserModel.object.create(
                            username=username,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            personal_number=personal_number,
                            is_staff=False,
                            is_superuser=False,
                        )
                    authenticate(request)
                    login(request, login_user)
                    return redirect(reverse_lazy('visitor'))
                elif status == 403:
                    return redirect(reverse_lazy("login"))
                else:
                    return super().dispatch(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

# Create your views here.
