from django.contrib import admin
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserCreationAdminForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)


class UserChangeAdminForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'password',)


@admin.register(User)
class AdvanceUserAdmin(UserAdmin):
    form = UserChangeAdminForm
    add_form = UserCreationAdminForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'email', 'birthday')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'), }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'email', 'birthday')}),
    )