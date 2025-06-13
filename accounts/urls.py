from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import logout_view

urlpatterns = [
   path('login/', views.login_view, name='login'),
   path('register/', views.register_view, name='register'),
   path('logout/', views.logout_view, name='logout'),
   path('dashboard/', views.dashboard_view, name='dashboard'),
   path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
   path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
   path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   path('edit-profile/', views.edit_profile, name='edit_profile'),
]
