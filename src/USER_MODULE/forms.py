from django import forms
from .models import Student, Faculty


class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'password',
            'confirm_password',
            'email',
            'registration_number',
            'branch',
            'year',
            'gender',
        )
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'})
        }


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = (
            'first_name',
            'last_name',
            'email',
            'id_number',
            'post',
            'department',
            'gender',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control col-3 display-inline'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control col-3 display-inline'}),
            'email': forms.TextInput(attrs={'class': 'form-control col-3'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control col-3'}),
            'department': forms.Select(attrs={'class': 'form-control col-3'}),
            'gender': forms.Select(attrs={'class': 'form-control col-3'})
        }

