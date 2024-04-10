from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name='', last_name='', **extra_fields):
        if not email:
            raise ValueError("Email address is required")
        email = self.normalize_email(email)
        if not password:
            raise ValueError("Password is required")
        if not first_name or not last_name:
            raise ValueError("Both first name and last name are required")
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, first_name='admin', last_name='admin', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, first_name, last_name, **extra_fields)