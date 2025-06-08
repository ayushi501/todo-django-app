from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from ToDoList import models
from ToDoList.models import ToDo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home(request):
    return render(request, 'signup.html')


def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        print(fnm, emailid, pwd)
        if User.objects.filter(username=fnm).exists():
            return HttpResponse("Username already exists. Try another.")
        else:
            myUser = User.objects.create_user(fnm, emailid, pwd)
            myUser.save()
        return redirect("/login")

    return render(request, 'signup.html')


def loginn(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm, pwd)
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request, userr)
            return redirect('/todopage')
        else:
            return redirect('/login')

    return render(request, "login.html")


@login_required(login_url='/login')
def todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        print(title)
        obj = ToDo(title=title, user=request.user)
        obj.save()
        res = ToDo.objects.filter(user=request.user).order_by('-date')
        return render('/todopage', {'res': res})
    res = ToDo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})


@login_required(login_url='/login')
def delete_todo(request, srno):
    if request.method == "POST":
        obj = ToDo.objects.get(srno=srno, user=request.user)
        obj.delete()
    return redirect('/todopage')


@login_required(login_url='/login')
def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = ToDo.objects.get(srno=srno, user=request.user)
        obj.title = title
        obj.save()
        return redirect('/todopage')

    obj = ToDo.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj': obj})


def signout(request):
    logout(request)
    return redirect('/login')
