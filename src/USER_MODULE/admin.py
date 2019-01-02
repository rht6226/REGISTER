from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission

from .models import SiteUser
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('user_id', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'date_of_birth', 'type')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('user_id', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender')}),
        ('Permissions', {'fields': ('is_admin', 'type')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'user_id')
    ordering = ('user_id', 'email', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender')
    filter_horizontal = ()


admin.site.register(SiteUser, UserAdmin)
admin.site.register(Permission)
admin.site.unregister(Group)
