from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    full_name = forms.CharField(
        required=True,
        label='NickName',
        max_length=50,
        error_messages={
            'required': 'Please enter your full name',
            'max_length': 'Please enter smaller than 50 lengh',
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'NickName',
            'class': 'form__input',
        })
    )
    phone_number = forms.CharField(
        required=True,
        label='PhoneNumber',
        max_length=11,
        widget=forms.TextInput(attrs={
            'placeholder': 'PhoneNumber',
            'class': 'form__input',
        })
    )
    email = forms.EmailField(
        required=True,
        label='EmailAddress',
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'class': 'form__input',
        })
    )
    password = forms.CharField(
        required=True,
        label='Password',
        min_length=8,
        widget=forms.TextInput(attrs={
            'type': 'password',
            'placeholder': 'Password',
            'class': 'form__input',
        })
    )
    confirm_password = forms.CharField(
        required=True,
        label='ConfirmPassword',
        min_length=8,
        widget=forms.TextInput(attrs={
            'type': 'password',
            'placeholder': 'ConfirmPassword',
            'class': 'form__input',
        })
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور باهم مغایرت دارد')


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='EmailAddress',
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'class': 'form__input',
        })
    )
    password = forms.CharField(
        required=True,
        label='Password',
        min_length=8,
        widget=forms.TextInput(attrs={
            'type': 'password',
            'placeholder': 'Password',
            'class': 'form__input',
        })
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='EmailAddress',
        widget=forms.EmailInput(attrs={
            'class': 'form__input',
            'placeholder': 'Email',
        })
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        required=True,
        label='NewPassword',
        min_length=8,
        widget=forms.TextInput(attrs={
            'type': 'password',
            'placeholder': 'Password',
            'class': 'form__input',
        })
    )
    confirm_password = forms.CharField(
        required=True,
        label='ConfirmPassword',
        min_length=8,
        widget=forms.TextInput(attrs={
            'type': 'password',
            'placeholder': 'ConfirmPassword',
            'class': 'form__input',
        })
    )
