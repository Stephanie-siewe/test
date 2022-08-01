from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import loader
from . import forms

# Create your views here.




def loginPage(request):
    form = forms.LoginForm()
    template = loader.get_template('autentication/login.html')
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],)
            if user is not None:
                login(request, user)
                messages.error(request, 'Authentification error')
    return HttpResponse(template.render(request, context={'form': form}))