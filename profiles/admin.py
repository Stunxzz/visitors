from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from profiles.models import Profile
superusers_group, created = Group.objects.get_or_create(name='Superusers')
staff_group, created = Group.objects.get_or_create(name='Staff')
content_type = ContentType.objects.get_for_model(Profile)
permissions = Permission.objects.filter(content_type=content_type)
superusers_group.permissions.set(permissions)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ('-date_joined',)

admin.site.register(Profile, ProfileAdmin)
