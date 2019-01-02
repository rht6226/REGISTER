from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.utils.html import strip_tags
# from .forms import UserCreationForm


class LoginView(View):

    def get(self, req):
        if not req.user.is_authenticated:
            context = {'title': 'Register | Login'}
            return render(req, 'authentication.html', context=context)
        else:
            return redirect('home')

    def post(self, req):
        username = strip_tags(req.POST['username'])
        password = strip_tags(req.POST['password'])
        user = authenticate(username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            error = 'User Does not Exists!'
            context = {'title': 'Register | User Not Found', 'error': error}
            return render(req, 'authentication.html', context=context)


class SelectUserView(View):

    def get(self, req):
        context = {'title': 'Sign Up'}
        return render(req, 'registration.html', context=context)


# class StudentRegistrationView(View):
#
#     def get(self, req):
#         student_form = StudentForm()
#         context = {'title': 'Register | Signup', 'form': student_form, 'user_type': 'Student'}
#         return render(req, 'student_registration.html', context=context)
#
#     def post(self, req):
#         form = StudentForm(req.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username= username, password=password)
#             login(req, user)
#             return redirect('home')
#         else:
#             context = {'title': 'Register | Try again', 'error': 'Something is not right!!'}
#             return render(req, 'student_registration.html', context=context)
#
#
# class FacultyRegistrationView(View):
#
#     def get(self, req):
#         faculty_form = FacultyForm()
#         context = {'title': 'Register | Signup', 'form': faculty_form, 'user_type': 'Faculty'}
#         return render(req, 'faculty_registration.html', context=context)


def logout_user(req):
    if req.method == 'POST':
        logout(req)
        return redirect('home')

