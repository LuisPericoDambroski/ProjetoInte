# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, register_view

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
