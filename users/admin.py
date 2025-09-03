from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "phone_number", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("profile_picture", "phone_number")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("profile_picture", "phone_number")}),
    )
    search_fields = ("username", "email", "phone_number")
    ordering = ("username",)

admin.site.register(CustomUser, CustomUserAdmin)
