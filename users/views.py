from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # tutaj mówimy django, że ma zapisać nowego użytkownika
        if form.is_valid():
            form.save()  # automatycznie tez haszuje hasło
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
