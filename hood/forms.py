from django import forms
from .models import *

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user','bio')

class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['location','occupants']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class BusinessForm(forms.ModelForm):
    class Meta:
        model  = Business
        exclude = ['user']