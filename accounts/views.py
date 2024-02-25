import random

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
from .models import OtpCode
from utils import send_otp_code


# Create your views here.
class UserRegisterView(View):
    form_class = UserRegistrationForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password']
            }
            messages.success(request, 'we send you a code', 'success')
            return redirect('accounts:user_verify_code')
        return redirect('home:home')
