from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from newsfeed.models import Post, Event
from .forms import EditProfileForm,UserProfileForm
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from newsfeed.forms import PostForm  # Correct import path
from .models import UserProfile

# Your view functions here

def dashboard(request):
    posts = Post.objects.all()  # Customize this query as needed
    events = Event.objects.all()  # Fetch events
    context = {
      'posts': posts,
      'events': events,
    }
    return render(request, 'newsfeed/dashboard.html', context)


@login_required
def profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return redirect('create_profile')  # Redirect to a profile creation view if not found
    return render(request, 'users/profile.html', {'user_profile': user_profile})


@login_required
def create_profile(request):
    try:
        # Check if the user already has a profile
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/setprofile.html', context)

def setprofile(request):
    if request.method == 'POST':
        UserProfile.objects.create(user=request.user)
        return redirect('profile')
    return render(request, 'users/setprole.html')
def login(request):
    return render(request, 'users/login.html', {})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('edit_profile')
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'edit_profile.html', context)


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('password_change_done')

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'





def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('profile')
    else:
        form = PostForm()
    return render(request, 'newsfeed/create_post.html', {'form': form})
