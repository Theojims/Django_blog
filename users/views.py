from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f' An account has been created for {username}')
            return redirect('blog-home')
    else:
        form = UserRegisterForm
    return render(request, "users/register.html", {'form':form})

# authentication/views.py


# def login_page(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             pass
#     return render(request, 'users/login.html', context={'form': form})


# def logout_view(request):
#     logout(request)
#     return render(request, 'users/logout.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')