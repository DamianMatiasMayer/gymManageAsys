from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Profile


#vistas principales


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

def delete_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    trainer.delete()
    return redirect('trainer')

def why(request):
    return render(request, "main/why.html")

def search(request):
    form = SearchForm(request.GET or None)
    trainers = Trainer.objects.all()
    members = Member.objects.all()
    classes = Class.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('search_query')
        if query:
            trainers = trainers.filter(nombre__icontains=query)
            members = members.filter(nombre__icontains=query)
            classes = classes.filter(titulo__icontains=query)

    context = {
        'form': form,
        'trainers': trainers,
        'members': members,
        'classes': classes
    }
    return render(request, 'main/search.html', context)


#registro


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

from django.contrib.auth import update_session_auth_hash

@login_required
def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    
    # Inicializar los formularios
    u_form = UserUpdateForm(instance=user)
    p_form = ProfileUpdateForm(instance=profile)
    password_form = PasswordChangeForm(user=user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        password_form = PasswordChangeForm(user=user, data=request.POST)
        
        if u_form.is_valid() and p_form.is_valid() and password_form.is_valid():
            u_form.save()
            p_form.save()
            user = password_form.save()
            update_session_auth_hash(request, user)  # Actualizar sesión con la nueva contraseña
            messages.success(request, 'Tu perfil y contraseña han sido actualizados.')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'password_form': password_form
    }

    return render(request, 'main/profile.html', context)





#acerca de mi 


def about(request):
    return render(request, 'main/about.html')