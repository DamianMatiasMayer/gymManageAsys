from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView

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

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, '¡Tu cuenta ha sido actualizada!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)