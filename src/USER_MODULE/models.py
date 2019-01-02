from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import SiteUserManager


class SiteUser(AbstractBaseUser):

    # Choices
    GENDER = (
        ('m', 'male'),
        ('f', 'female'),
        ('c', 'cannot disclose')
    )

    TYPE = (
        ('s', 'student'),
        ('f', 'faculty'),
    )

    # Information Fields
    user_id = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100, blank=False, default='')
    last_name = models.CharField(max_length=100, blank=False, default='')

    type = models.CharField(max_length=1, choices=TYPE, blank=True, default='s')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    middle_name = models.CharField(max_length=30, default='', blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='c')
    date_of_birth = models.DateField(blank=True, default='1998-11-01')
    profile_image = models.ImageField(upload_to='user/', blank=True)

    # AbstractBaseUser settings
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email', 'type']

    objects = SiteUserManager()

    # Metadata
    class Meta:
        default_permissions = ()
        permissions = (
            ("add_user", "add user"),
            ("change_user", "update user"),
            ("delete_user", "delete user"),
            ("view_user", "view user"),
        )
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # Methods
    def get_full_name(self):
        # get the full name of the user
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    def __str__(self):
        return self.user_id + ' | ' + self.get_full_name()

    @property
    def image_url(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return r"/static/add_user.png"

    # Permissions
    @property
    def is_staff(self):
        """
        Is the user a member of the staff ?
        :return:
        """
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin







