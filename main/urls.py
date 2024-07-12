from django.contrib.auth import views as auth_views
from django.urls import path, include
from main.views import *
from . import views

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('trainer/', trainer, name="trainer"),
    path('why/', why, name="why"),
    path('search/', search, name='search'),
    
    path('delete_trainer/<int:trainer_id>/', delete_trainer, name='delete_trainer'),


    #login/logout/modificacion
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    #registro
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
