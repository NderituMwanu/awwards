from django import forms
from .models import *

class Post_project(forms.ModelForm):

    class Meta:
        model = Post
        exclude = [
            'updated_on',
            'slug',
            'created_on', 
        ]



class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =[
            'user'
        ]


class UserProfile(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            'username'
            
        ]