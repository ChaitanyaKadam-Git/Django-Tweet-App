from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 9, 'placeholder': 'What\'s happening?'}),
            'photo': forms.ClearableFileInput(attrs={'multiple': False}),
        }
        labels = {
            'text': 'Tweet',
            'photo': 'Upload Photo (optional)',
        }
        
class UserRestrictionForm(UserCreationForm):
   email = forms.EmailField(required=False)
   class Meta:
            model = User
            fields =('username', 'email', 'password1', 'password2') 
       