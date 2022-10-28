from django.shortcuts import render, redirect
from .models import List
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('func')
        else:
            messages.info(request,'username or password is incorrrect')    
            return redirect('loginpage')
    context={}    
    return render(request,'todo/login.html',context)

def registerpage(request):
    form= userform()
    if request.method=="POST":
        form= userform(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'successfully registered new user',user)
            return redirect('loginpage')
    return render(request, 'todo/register.html',{'form':form})


def func(request):
    lists =List.objects.filter(Userr=request.user)
    form = apply()
    if request.method == 'POST':
        form = apply(request.POST)  
        if form.is_valid():
            form.save()
    return render(request, 'todo/first.html',{'lists': lists , 'form': form})          

def deletestuff(request, pk):
    lol=List.objects.get(id=pk)
    if request.method == 'POST':
        lol.delete()
        return redirect('func')
    return render(request, 'todo/delete.html',{'lol':lol} )

def updatestuff(request ,pk):
    lol =List.objects.get(id=pk)
    form=apply(instance = lol)
    if request.method == 'POST':
        form=apply(request.POST, instance=lol)
        if form.is_valid():
            form.save()
            return redirect('func')
    return render(request, 'todo/update.html', {'form':form})
