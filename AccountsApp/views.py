from django.shortcuts import render, redirect
from django.urls import reverse
from AccountsApp.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from .models import Users
from django.http import HttpResponse, Http404
from django.utils.crypto import get_random_string


# Create your views here.
def success(request):
    return render(request, 'succses.html')


def index(request):
    return render(request, 'Home/index.html')


def Register(request):
    register_page = RegisterForm(request.POST)
    if register_page.is_valid():
        full_name = register_page.cleaned_data.get('full_name')
        phone = register_page.cleaned_data.get('phone_number')
        email = register_page.cleaned_data.get('email')
        user: bool = Users.objects.filter(email__iexact=email).exists()
        password = register_page.cleaned_data.get('password')
        confirm_password = register_page.cleaned_data.get('confirm_password')
        if user:
            register_page.add_error('email', 'you have already registered')
        else:
            new_user = Users(
                username=full_name,
                phone=phone,
                confirm_code=get_random_string(48),
                email=email,
                is_active=False,
            )
            new_user.set_password(password)
            new_user.save()
            # return redirect(reverse(''))

    context = {
        'register_page': register_page,
    }
    return render(request, 'RegisterPage/Register.html', context)


def Login(request):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        user_email = login_form.cleaned_data.get('email')
        user_password = login_form.cleaned_data.get('password')
        user: Users = Users.objects.filter(email__iexact=user_email).first()
        if user is not None:
            if not user.is_active:
                login_form.add_error('email', 'حساب کاربری شما فعال نمی باشد')
            else:
                is_password_correct = user.check_password(user_password)
                if is_password_correct:
                    Login(request, Users)
                    return redirect(reverse('Home-page'))
                else:
                    login_form.add_error('email', 'ایمیل یا کلمه عبور صحیح نمی باشد')
    else:
        login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

    context = {
        'login_form': login_form
    }

    return render(request, 'Accounts/login_page.html', context)


def ForgotPassword(request):
    return render(request, 'ForgotPassword/ForgetPassword.html')


def ResetPassword(request):
    return render(request, 'ResetPassword/ResetPassword.html')
