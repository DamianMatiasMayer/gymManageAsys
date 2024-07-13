from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', main_views.index, name='index'),
    path('contact/', main_views.contact, name='contact'),
    path('trainer/', main_views.trainer, name='trainer'),
    path('why/', main_views.why, name='why'),
    path('search/', main_views.search, name='search'),
    path('delete_trainer/<int:trainer_id>/', main_views.delete_trainer, name='delete_trainer'),
    
    path('register/', main_views.register, name='register'),
    path('profile/', main_views.profile, name='profile'),
    
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    #acerca de mi 
    path('about/', main_views.about, name='about'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)