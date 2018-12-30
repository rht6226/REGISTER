from django.urls import path
from .views import LoginView, RegistrationView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('get_started/', RegistrationView.as_view(), name='signup'),
]
