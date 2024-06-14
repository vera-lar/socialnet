
from django.shortcuts import render, redirect
#get_object_or_404

from django.contrib import messages



from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm
from newsfeed.models import News
from newsfeed.forms import NewsForm
from .forms import EditProfileForm,UserProfileForm


from django.contrib.auth.forms import UserCreationForm


# Your view functions here

#def profile(request, username):
    #user = get_object_or_404(User, username=username)
    #return render(request, 'users/profile.html', {'user_profile': user})





def create_profile(request):
    try:
        # Check if the user already has a profile
        profile = request.user.userprofile
    except Profile.DoesNotExist:
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
    return render(request, 'dashboard', context)


#def edit_profile(request):
    #if request.method == 'POST':
       # profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
      #  if profile_form.is_valid():
         #   profile_form.save()
       #     return redirect('profile', username=request.user.username)
    #else:
     #   profile_form = ProfileForm(instance=request.user.profile)
    #return render(request, 'users/edit_profile.html', {
     #   'profile_form': profile_form
   # })


def dashboard(request):
    if request.method == 'POST':
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            news = news_form.save(commit=False)
            news.user = request.user
            news.save()
            return redirect('dashboard')
    else:
        news_form = NewsForm()

    posts = News.objects.all()
    events = []  # Fetch events using Google News API or other sources

    context = {
        'news_form': news_form,
        'posts': posts,
        'events': events,
    }
    return render(request, 'newsfeed/dashboard.html', context)