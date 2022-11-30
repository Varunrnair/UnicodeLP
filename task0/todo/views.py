from django.shortcuts import render, redirect
from .models import List
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required , user_passes_test


def loginpage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request, email=email, password=password)
        print(user,email)
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
        print("Entered")
        form= userform(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('email')
            messages.success(request,'successfully registered new user',user)
            return redirect('loginpage')
        print(form.errors)
    return render(request, 'todo/register.html',{'form':form})

def logoutuser(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='loginpage')
def func(request):   
    user =request.user
    form = apply()
    if request.method == 'POST':
        form = apply(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            print(form.data)
    return render(request, 'todo/first.html',{'form': form})     
 
@login_required(login_url='loginpage')
def showlist(request):
    lists =List.objects.filter(user=request.user)
    return render(request, 'todo/list.html',{'lists':lists})    

@login_required(login_url='loginpage')
def deletestuff(request, pk):
    lol=List.objects.get(id=pk)
    if request.method == 'POST':
        lol.delete()
        return redirect('func')
    return render(request, 'todo/delete.html',{'lol':lol} )

@login_required(login_url='loginpage')
def updatestuff(request ,pk):
    lol =List.objects.get(id=pk)
    form=apply(instance = lol)
    if request.method == 'POST':
        form=apply(request.POST, instance=lol)
        if form.is_valid():
            form.save()
            return redirect('func')
    return render(request, 'todo/update.html', {'form':form})
