from django.urls import path
from .views import LoginView, SelectUserView, StudentRegistrationView, FacultyRegistrationView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('get_started/', SelectUserView.as_view(), name='signup'),
    path('get_started/student', StudentRegistrationView.as_view(), name='student_signup'),
    path('get_started/faculty', FacultyRegistrationView.as_view(), name='faculty_signup'),
]
