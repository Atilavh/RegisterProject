from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    full_name = forms.CharField(
        required=True,
        label='NickName',
        max_length=50,
    )
    phone_number = forms.CharField(
        required=True,
        label='PhoneNumber',
        max_length=11
    )
    email = forms.EmailField(
        required=True,
        label='EmailAddress',

    )
    password = forms.CharField(
        required=True,
        label='Password',
        min_length=8,
    )
    confirm_password = forms.CharField(
        required=True,
        label='ConfirmPassword',
        min_length=8,
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

    )
    password = forms.CharField(
        required=True,
        label='Password',
        min_length=8,
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='EmailAddress',
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        required=True,
        label='NewPassword',
        min_length=8,
    )
    confirm_password = forms.CharField(
        required=True,
        label='ConfirmPassword',
        min_length=8,
    )
