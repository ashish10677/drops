from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Files

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class FilesForm(forms.ModelForm):
    
    class Meta:
        model = Files
        fields = ("title", "file_name")

class SplitForm(forms.Form):

    CHOICES = [(i,i) for i in range(1,10)]
    number_of_chunks = forms.ChoiceField(required=False, choices=CHOICES)

