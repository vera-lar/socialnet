from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile # Import your UserProfile model if you have one
from .models import Post

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email'] 

from django import forms
from .models import Changepassword

class ChangepasswordForm(forms.ModelForm):
    newpassword1 = forms.CharField(widget=forms.PasswordInput, max_length=100)
    newpassword2 = forms.CharField(widget=forms.PasswordInput, max_length=100)

    class Meta:
        model = Changepassword
        fields = ['newpassword1', 'newpassword2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("newpassword1")
        password2 = cleaned_data.get("newpassword2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'bio', 'location', 'birth_date']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']#'post_type', 'media_url'
from .models import Profile  # Adjust this import according to your model's location


from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['is_online', 'bio', 'location', 'birth_date']  # Add your profile fields here
