
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
    search_query = forms.CharField(label='Search')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['nombre', 'email', 'telefono', 'mensaje']
        
#registro
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'avatar']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']