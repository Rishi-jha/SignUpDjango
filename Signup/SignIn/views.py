# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignInForm
# Create your views here.
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/home/')
    else:
        form = SignInForm()
        
    return render(request, 'SignIn/signin.html', {'form': form})
