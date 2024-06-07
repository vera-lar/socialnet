# Inside forms.py

from django import forms

class SubscribeForm(forms.Form):
    email = forms.EmailField(label='Email')
