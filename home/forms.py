# Inside forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SubscribeForm(forms.Form):
    email = forms.EmailField(label='Email')

from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    platform = forms.CharField(max_length=50)
    library = forms.CharField(max_length=50)
    files = forms.FileField()

    class Meta:
        model = Project
        fields = ['title', 'description', 'platform', 'library', 'files']


# forms.py

from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
  

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SignInForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
# forms.py


from .models import CommunityPost

class CommunityPostForm(forms.ModelForm):
    class Meta:
        model = CommunityPost
        fields = ['title', 'content']
# forms.py
from .models import CommunityEvent
class CommunityEventForm(forms.ModelForm):
    class Meta:
        model = CommunityEvent
        fields = ['title', 'description', 'date']
# forms.py
from.models import ForumThread, ForumPost
class ForumThreadForm(forms.ModelForm):
    class Meta:
        model = ForumThread
        fields = ['title']

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['content']

# forms.py
from .models import Tutorial
class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['title', 'content']
