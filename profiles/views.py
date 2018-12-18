from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return redirect('profiles:login')
    else:
        form = UserRegisterForm()
    return render(request, 'profiles/register.html', {'form': form})


@login_required
def profile(request):
    context = {'user': request.user}
    return render(request, 'profiles/profile.html', context)


def profileUpdate(request):
    form = ProfileUpdateForm(request.POST or None, instance=request.user.profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved!')
            return redirect('profiles:profile')
    return render(request, 'profiles/edit.html', {'form': form})
