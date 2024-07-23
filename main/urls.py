from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    
    #urls principales
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
    
    #CRUD para Trainer
    path('trainers/', main_views.trainer_list, name='trainer_list'),
    path('trainers/<int:pk>/', main_views.trainer_detail, name='trainer_detail'),
    path('trainers/new/', main_views.trainer_create, name='trainer_create'),
    path('trainers/<int:pk>/edit/', main_views.trainer_update, name='trainer_update'),
    path('trainers/<int:pk>/delete/', main_views.trainer_delete, name='trainer_delete'),

    #CRUD para Member
    path('members/', main_views.member_list, name='member_list'),
    path('members/<int:pk>/', main_views.member_detail, name='member_detail'),
    path('members/new/', main_views.member_create, name='member_create'),
    path('members/<int:pk>/edit/', main_views.member_update, name='member_update'),
    path('members/<int:pk>/delete/', main_views.member_delete, name='member_delete'),
    
     #CRUD para Class
    path('classes/', main_views.class_list, name='class_list'),
    path('classes/<int:pk>/', main_views.class_detail, name='class_detail'),
    path('classes/new/', main_views.class_create, name='class_create'),
    path('classes/<int:pk>/edit/', main_views.class_update, name='class_update'),
    path('classes/<int:pk>/delete/', main_views.class_delete, name='class_delete'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)