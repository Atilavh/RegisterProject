from django.urls import path
from . import views

urlpatterns = [
    path('success', views.success, name='success'),
    path('', views.index, name='index'),
    path('Account/Rgister', views.Register, name='RegisterForm'),
    path('activeaccount/<confirm>', views.confirm_register, name='confirm'),
    path('Account/Login', views.Login, name='LoginForm'),
    path('Account/ForgetPassword', views.ForgotPassword, name='ForgetPassword'),
    path('Account/ResetPassword', views.ResetPassword, name='ResetPassword'),
]
