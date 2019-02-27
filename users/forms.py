from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField()
    def clean_username(self):
        name_l = self.cleaned_data['username']
        if name_l == "admin" or name_l == "author":
            raise ValidationError("'Author name can't be 'admin/author'")
        return self.cleaned_data.get('username','')
    def clean_email(self):
        if (self.cleaned_data.get('email', '')
                .endswith('hotmail.com')):
            raise ValidationError("Invalid email address.")
        return self.cleaned_data.get('email', '')
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')