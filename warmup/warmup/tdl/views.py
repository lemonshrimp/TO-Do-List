from models import *
from django.shortcuts import render_to_response
from django.contrib import auth

def index(request): 
    lists = tdList.objects.all() 
    tdElems = []
    for elem in lists:
     tdElems.append(To_do.objects.filter(inList = elem))
     
    return render_to_response('index.html', {'items': lists, 'content': tdElems})

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/todo/")
    else:
        # Show an error page
        return HttpResponseRedirect("")

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("")


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })
