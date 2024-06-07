from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile  # Import your UserProfile model if you have one
from .models import Post

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'bio', 'location', 'birth_date']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']#'post_type', 'media_url'
