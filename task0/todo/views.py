from django.shortcuts import render, redirect
from .models import List
from .forms import apply

def func(request):
    lists =List.objects.all()
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
