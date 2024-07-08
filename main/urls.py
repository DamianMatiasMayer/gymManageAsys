
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('trainer/', trainer, name="trainer"),
    path('why/', why, name="why"),
    path('search/', search, name='search'),
    
    path('delete_trainer/<int:trainer_id>/', delete_trainer, name='delete_trainer'),
]
