
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SubscribeForm
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'home/home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'home/login.html', {'error': 'Invalid credentials'})
    return render(request, 'home/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
   
 # Save the email address to your database or perform other actions
 # Redirect to a thank you page or display a confirmation message
            
 


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Process the subscription or send confirmation email if needed
            # Redirect to a confirmation page after successful subscription
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
def profile(request):
    return render(request, 'users/profile.html', {})