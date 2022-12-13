from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.views import View

from main.forms import AuthenticationForm, OrderForm

from main.forms import UserChangeForm

from main.forms import UserCreationForm


def index(request):
    return render(request, 'main/layout.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def demo(request):
    return render(request, 'main/demo.html')


class MyLoginView(LoginView):
    form_class = AuthenticationForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect('home')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class OrderAdd(View):
    template_name = 'main/demo.html'

    def get(self, request):
        user = request.user
        context = {
            'form': OrderForm(initial={'createdBy': user})
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'form': form,
            'answ': "Данные заполнены неверно"
        }
        return render(request, self.template_name, context)
