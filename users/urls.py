from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    DashboardView,ProfileView, ProfileEditView, CustomPasswordChangeView,
    CustomPasswordResetView, CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView, CustomPasswordResetCompleteView,
    SignUpView
)

urlpatterns = [
    # Login & Logout
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Signup
    path('signup/', SignUpView.as_view(), name='signup'),

    # Profile
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('profile/change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),      
    
    # Reset Password (email)
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
