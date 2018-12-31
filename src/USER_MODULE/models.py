from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER = (
        ('m', 'male'),
        ('f', 'female'),
        ('c', 'cannot disclose')
    )

    TYPE = (
        ('s', 'student'),
        ('f', 'faculty')
    )

    # Required
    type = models.CharField(max_length=1, choices=TYPE, blank=True, default='s')

    # optional
    middle_name = models.CharField(max_length=30, default='', blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='c')
    date_of_birth = models.DateField(blank=True, default='1998-11-01')
    profile_image = models.ImageField(upload_to='user/', blank=True)

    def get_full_name(self):
        # get the full name of the user
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    def __str__(self):
        return self.username + ' | ' + self.get_full_name()

    @property
    def image_url(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return r"/static/add_user.png"

    class Meta:
        default_permissions = ()
        permissions = (
            ("add_user", "add user"),
            ("change_user", "update user"),
            ("delete_user", "delete user"),
            ("view_user", "view user"),
        )


class Student(User):

    BRANCH = (
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communications Engineering'),
        ('IT', 'Information Technology'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('CHE', 'Chemical Engineering'),
        ('PIE', 'Production and Industrial Engineering'),
        ('BT', 'Biotechnology'),
    )

    YEAR = (
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Final Year')
    )

    # During Registration
    registration_number = models.CharField(max_length=8, unique=True, blank=False)
    branch = models.CharField(max_length=3, blank=False, choices=BRANCH, default='ECE')
    year = models.PositiveIntegerField(max_length=1, blank=False, choices=YEAR, default=1)

    # After Registration
    father = models.CharField(max_length=70, default='', blank=True)
    mother = models.CharField(max_length=70, default='', blank=True)

    address = models.CharField(max_length=150, blank=True, default='')
    street = models.CharField(max_length=75, blank=True, default='')
    landmark = models.CharField(max_length=75, blank=True, default='')
    zip = models.CharField(max_length=15, blank=True, default='')
    state = models.CharField(max_length=40, blank=True, default='')
    country = models.CharField(max_length=40, blank=True, default='')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Faculty(User):

    DEPARTMENT = (
        ('CSED', 'Computer Science and Engineering Department'),
        ('ECED', 'Electronics and Communications Engineering Department'),
        ('MED', 'Mechanical Engineering Department'),
        ('CED', 'Civil Engineering Department'),
        ('CHD', 'Chemistry Department'),
        ('MD', 'Mathematics Department'),
        ('PD', 'Physics Department'),
        ('BTD', 'Biotechnology Department'),
        ('AMD', 'Applied Mechanics Department'),
    )

    # During Registration
    id_number = models.CharField(max_length=10, unique=True, blank=False)
    post = models.CharField(max_length=40, blank=True, default='')
    department = models.CharField(max_length=5, choices=DEPARTMENT)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'


