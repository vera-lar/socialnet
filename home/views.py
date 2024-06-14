
# Create your views here.
from .forms import SubscribeForm
from django.core.mail import send_mail
from django.conf import settings
from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContactForm
from .forms import SignUpForm, SignInForm  # Assuming these forms are defined in forms.py
from django.contrib.auth.forms import UserCreationForm,authenticate



def home(request):
    signup_form = SignUpForm()
    signin_form = SignInForm()
    return render(request, 'home/home.html', {'signup_form': signup_form, 'signin_form': signin_form
        })

def about(request):
    return render(request, 'home/about.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                f'Contact Form Submission from {name}',
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
            )
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    
    return render(request, 'home/contact.html', {'form': form})



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')



   
 # Save the email address to your database or perform other actions
 # Redirect to a thank you page or display a confirmation message
            


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
       form =authenticate(request, data=request.POST)
       if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
       else:
        form =authenticate()
        return render(request, 'home/signin.html', {'form': form})



def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
             #Process the subscription or send confirmation email if needed
             #Redirect to a confirmation page after successful subscription
            return redirect('confirmation')
    else:
        form = SubscribeForm()  # Create a new form instance for GET requests
    return render(request, 'home/subscribe.html', {'form': form })

def confirmation(request):
    return render(request, 'home/confirmation.html', {})
# views.py


def send_confirmation_email(email):
    subject = 'Confirmation Email'
    message = 'Thank you for subscribing!'
    sender_email = settings.EMAIL_HOST_USER
    recipient_email = email
    send_mail(subject, message, sender_email, [recipient_email])

from newsfeed.models import Post, Event
from users.forms import UserForm, ProfileForm
from users.models import Profile


def dashboard(request):
    posts = Post.objects.all()  # Customize this query as needed
    events = Event.objects.all()  # Fetch events
    context = {
      'posts': posts,
      'events': events,
    }
    return render(request, 'newsfeed/dashboard.html', context)

def edit_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'users/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy

from users.models import UserProfile, Changepassword

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'users/change_password_change.html'
    success_url = reverse_lazy('change_password_change_done')

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/change_password_change_done.html'


from newsfeed.forms import PostForm  # Correct import path


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
    return render(request, 'users/create_post.html', {'form': form})


from users.forms import ChangepasswordForm
def profile(request):
    try:
        user_profile = request.user.userprofile
    except Profile.DoesNotExist:
        return redirect('create_profile')  # Redirect to a profile creation view if not found
    return render(request, 'users/profile.html', {'user_profile': user_profile})


def change_password(request):
    if request.method == 'POST':
        form = ChangepasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('newpassword')
            # Assuming you are changing the password for the logged-in user
            user = request.user
            user.set_password(new_password)
            user.save()
            return redirect('login')  # Redirect to login page after password change
    else:
        form = ChangepasswordForm()

    return render(request, 'users/change_password.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')
