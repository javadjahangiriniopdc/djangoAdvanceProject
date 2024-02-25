from django.contrib import admin
from django.urls import path, include

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register')
]
