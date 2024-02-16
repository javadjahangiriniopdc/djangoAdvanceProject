from django.contrib import admin
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import Group


# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'phone_number', 'fullname', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'fullname', 'password')}),
        ('Permission', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'fullname', 'password1', 'password2')}),
    )

    search_fields = ('email', 'phone_number', 'fullname')
    ordering = ('fullname',)
    filter_horizontal = []


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
