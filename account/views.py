from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import forms
from .import models
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def signup(request):
    if request.method == 'POST':
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            choice = form.cleaned_data['user_choice']

            user = authenticate(username=username, password=password)
    
            if choice == 'admin':
                models.AdminUser.objects.create(user=user)
            elif choice == 'frontend':
                models.FrontEndUser.objects.create(user=user)
            
            return redirect('home')
    else:
        form = forms.UserCreateForm()
    return render(request, 'account/signup.html', {'form': form})
   
