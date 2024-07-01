
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('trainer/', trainer, name="trainer"),
    path('why/', why, name="why"),
]
