from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


def register(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created.')
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


# class UserProfileListView(LoginRequiredMixin, ListView):
#     model = Profile
#     template_name = 'account/profile.html'
#     ordering = ['-datetime']

@login_required
def profile(request):
    return render(request,'account/profile.html')


def profileupdate(request):
    if(request.method == 'POST'):
        pform = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        if pform.is_valid():
            pform.save()
            return redirect('profile')

    else:
        pform = ProfileUpdateForm(instance = request.user.profile)

    return render(request, 'account/profileupdate.html', {'form': pform})
