from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Users
from .forms import UsersForm




def index(request):
    message = Users.objects.order_by('-id')
    return render(request, 'main/index.html', {'message':message})
def chat(request):
    error = ''
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неправильно'

    form = UsersForm()
    data={
        'form':form,
        'error': error
    }
    return render(request, 'main/chat.html',data)
def first(request):
    message = Users.objects.order_by('-id')
    return render(request, 'main/firstroom.html', {'message':message})
def second(request):
    message = Users.objects.order_by('-id')
    return render(request, 'main/secondroom.html', {'message':message})
def third(request):
    message = Users.objects.order_by('-id')
    return render(request, 'main/thirdroom.html', {'message':message})
