from django.shortcuts import render
from django.views.generic import TemplateView, View


class HomeView(TemplateView):

    def get(self, req):
        context = {'title': 'Register | Home'}
        return render(req, 'index.html', context=context)
