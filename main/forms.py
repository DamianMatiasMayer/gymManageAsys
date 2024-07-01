
from django import forms
from .models import Member
from .models import Trainer


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['nombre', 'telefono', 'mensaje']

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['nombre', 'experiencia', 'tarifa']

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['nombre', 'email', 'telefono', 'mensaje']