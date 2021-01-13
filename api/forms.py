from django import forms
from .models import CustomUser


class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone', 'tag']



