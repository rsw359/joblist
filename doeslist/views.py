from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .register_form import User_Registration_Form
from django.http import HttpResponse



def home(request):
    return render(request, 'doeslist/base.html')

def register(request):
    if request.method == 'POST':
        form = User_Registration_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = User_Registration_Form()
    return render(request, 'doeslist/register.html', {'form': form})




    