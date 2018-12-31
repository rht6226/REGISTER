from django.contrib.auth.backends import ModelBackend
from .models import Student, Faculty


class StudentOrFaculty(ModelBackend):
    """
    Backend using ModelBackend, but attempts to "downcast"
    the user into a Student or Faculty.
    """

    def authenticate(self, *args, **kwargs):
        return self.downcast_user_type(super().authenticate(*args, **kwargs))

    def get_user(self, *args, **kwargs):
        return self.downcast_user_type(super().get_user(*args, **kwargs))

    def downcast_user_type(self, user):
        try:
            student = Student.objects.get(pk=user.pk)
            return student
        except:
            pass

        try:
            faculty = Faculty.objects.get(pk=user.pk)
            return faculty
        except:
            pass

        return user