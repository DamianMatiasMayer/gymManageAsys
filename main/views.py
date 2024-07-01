from django.shortcuts import render, redirect
from .models import *
from .forms import MemberForm
from .forms import TrainerForm
from .forms import SearchForm


def index(request):
    return render(request, "main/index.html")

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()              
            return redirect('index')  
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = TrainerForm()
    
    trainers = Trainer.objects.all()
    context = {
        'form': form,
        'trainers': trainers,
    }
    return render(request, 'main/trainer.html', context)

def why(request):
    return render(request, "main/why.html")


def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('search_query')
            
            trainers = Trainer.objects.filter(nombre__icontains=query)
            members = Member.objects.filter(nombre__icontains=query)
            classes = Class.objects.filter(titulo__icontains=query)
            
            context = {
                'trainers': trainers,
                'members': members,
                'classes': classes,
                'query': query,
            }
            return render(request, 'main/search_results.html', context)
    else:
        form = SearchForm()
    
    return render(request, 'main/search.html', {'form': form})
