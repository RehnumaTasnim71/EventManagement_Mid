from django.views.generic import DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .forms import CustomUserCreationForm

# Use the custom user model
User = get_user_model()


# ------------------------------
# Dashboard View
# ------------------------------
class DashboardView(LoginRequiredMixin, TemplateView):
    # default template
    template_name = 'users/dashboard/default.html'

    def get_template_names(self):
        user = self.request.user
        if user.is_superuser:
            return ['users/dashboard/admin.html']
        elif user.groups.filter(name='Organizer').exists():
            return ['users/dashboard/organizer.html']
        elif user.groups.filter(name='Participant').exists():
            return ['users/dashboard/participant.html']
        else:
            return ['users/dashboard/default.html']


# ------------------------------
# Profile Views
# ------------------------------
class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'

    def get_object(self):
        return self.request.user


class ProfileEditView(UpdateView):
    model = User
    fields = ['username', 'email', 'profile_picture']
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


# ------------------------------
# Password Views
# ------------------------------
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('profile')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


# ------------------------------
# Signup View
# ------------------------------
class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')



