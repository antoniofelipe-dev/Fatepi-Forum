from django.contrib import admin
from .models import Users, Curso
from django.contrib.auth import admin as admin_auth_django
from .forms import UserChangeForm, UserCreationForm


admin.site.register(Curso)
admin.site.register(Users)