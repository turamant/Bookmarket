from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
