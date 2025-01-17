
from django import forms
from .models import Member, Trainer, Class, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['nombre', 'telefono', 'mensaje']

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['nombre', 'experiencia_anios']
        
class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='Buscar')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['nombre', 'email', 'telefono', 'mensaje']
        
#registro
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
        
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['titulo', 'descripcion', 'entrenador', 'miembros']