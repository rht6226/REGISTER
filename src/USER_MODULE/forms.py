from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import SiteUser as User


class UserCreationForm(forms.ModelForm):
    """ A form for creating new users. Includes all the required
    fields, plus a repeated password. """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'user_id',
            'email',
            'first_name',
            'last_name',
            'type',
        )

    def clean_password(self):
        # Checks if both the passwords are entered and are same
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Nigga, the passwords do'nt match")
        else:
            return password1

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'user_id',
            'email',
            'first_name',
            'middle_name',
            'last_name',
            'type',
            'gender',
            'date_of_birth',
            'profile_image'
        )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


