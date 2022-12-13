from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from main.models import Order

User = get_user_model()


class AuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class OrderForm(forms.ModelForm):
    FIO = forms.CharField(
        label=_("ФИО"),
        widget=forms.TextInput()
    )

    tariff = forms.CharField(
        label=_("Тариф"),
        widget=forms.TextInput()
    )

    datetime = forms.DateTimeField(
        label=_("Дата"),
        widget=forms.DateTimeInput()
    )

    class Meta:
        model = Order
        fields = ('createdBy', 'FIO', 'tariff', 'datetime')
        widgets = {'createdBy': forms.HiddenInput()}
