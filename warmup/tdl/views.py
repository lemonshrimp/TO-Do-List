from models import To_do
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext

def todo(request, provedUser): 
    lists = tdList.objects.filter(user=provedUser)
    totalList = []
    for lelem in lists:
     totalList.append(To_do.objects.filter(inList = lelem)
    #items = To_do.objects.all() , 
 
    return render('todo.html', {'items': lists, 'finalList': totalList}, context_instance=RequestContext(request))

def index(request): 
 
    return render_to_response('index.html', context_instance=RequestContext(request))


def login(request):
    c = {}
    c.update(csrf(request))
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
           login(request,user)
           return render_to_response('todo.html', context_instance=RequestContext(request))
    else:
        return render_to_response('index.html', context_instance=RequestContext(request))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

@login_required
def delete_td(request,td_id):

    td = To_do.objects.get(id=To_do_id)
    td.delete()
    return HttpResponse("true")

from datetime import datetime
@login_required
def add_td(request):

    td_Title = request.GET.get('title')
    td_Date = datetime.strptime(request.GET.get('Date'),"%m/%d/%Y")
    td_Content = request.GET.get('Content')
    new_td = td(Title=td_Title,Date=td_Date,Content=td_Content,user=request.user)
    new_td.save()
    return HttpResponse(new_td.id)
