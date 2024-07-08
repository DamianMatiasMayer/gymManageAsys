from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages

def index(request):
    return render(request, "main/index.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gracias por contactarnos. Nos pondremos en contacto contigo pronto.')
            return redirect('contact')  
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})


def trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer')
    else:
        form = TrainerForm()
    
    trainers = Trainer.objects.all()
    return render(request, 'main/trainer.html', {'form': form, 'trainers': trainers})



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

def delete_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    trainer.delete()
    return redirect('trainer')