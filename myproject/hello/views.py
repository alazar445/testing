from django.shortcuts import render, redirect
from .forms import PersonForm

def person_create(request):
    form = PersonForm(request.POST or None)  # simpler handling
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('success')
        
    return render(request, 'simpleform/person_form.html', {'form': form})

def success(request):
    return render(request, 'simpleform/success.html')
