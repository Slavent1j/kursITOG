from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from main.models import Order

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_role', 'phone')
    UserAdmin.fieldsets += (('Extra Fields', {'fields': ('user_role', 'phone', 'address')}),)


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('FIO', 'tariff', 'datetime')
    #Order.fieldsets += (('Extra Fields', {'fields': ('FIO', 'tariff', 'datetime')}),)
