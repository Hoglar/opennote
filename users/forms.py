from django import forms
from django.core import validators

class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, label="Username")
    password = forms.CharField(
        label="Password",
        min_length=8,
        widget=forms.PasswordInput
    )

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        label="Username",
        validators=[
            validators.RegexValidator(
                regex=r'^\S+$',
                message="Username cannot contain spaces."
            )
        ]
        )
    email = forms.EmailField(label="Email")
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        min_length=8,
        validators=[
            validators.MinLengthValidator(8, "Password must be atleast 8 characters long.")
        ]
    )
    password_confirmation = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput
    )
    
    def clean(self):
        cleaned_data = super().clean() 
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            self.add_error('password_confirmation', "Passwords do not match")
