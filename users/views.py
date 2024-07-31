from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdate, ProfileUpdate

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)

def profile(request):
    if request.method == 'POST':
        user_up_date = UserUpdate(request.POST, instance=request.user)
        profile_up_date = ProfileUpdate(request.POST, request.FILES, instance=request.user.profilemodel)
        if user_up_date.is_valid() and profile_up_date.is_valid():
            user_up_date.save()
            profile_up_date.save()
            return redirect('users-profile')
    else:
        user_up_date = UserUpdate(instance=request.user)
        profile_up_date = ProfileUpdate(instance=request.user.profilemodel)
    
    context = {
        'u_up': user_up_date,
        'p_up': profile_up_date
    }
    return render(request, 'users/profile.html', context)
