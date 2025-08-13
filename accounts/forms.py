from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })

class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length="50",
        widget=forms.TextInput(
            attrs={'placeholder': 'Username', 'class': 'form-control'}
        )
    )
    password = forms.CharField(
        max_length="50", 
        widget=forms.PasswordInput(
            attrs={"placeholder": 'Password', 'class': 'form-control'}
        )
    )