from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.utils.html import strip_tags


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
        User = authenticate(username=username, password=password)

        if User is not None:
            login(req, User)
            return redirect('home')
        else:
            error = 'User Does not Exists!'
            context = {'title': 'Register | User Not Found', 'error': error}
            return render(req, 'authentication.html', context=context)


class RegistrationView(View):

    def get(self, req):
        context = {'title': 'Register | Signup'}
        return render(req, 'registration.html', context=context)


def logout_user(req):
    if req.method == 'POST':
        logout(req)
        return redirect('home')

