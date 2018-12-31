from django.contrib import admin
from .models import User, Student, Faculty
from django.contrib.auth.models import Permission

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Permission)
