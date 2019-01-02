from django.contrib.auth.models import BaseUserManager


class SiteUserManager(BaseUserManager):

    def create_user(self, user_id, email, type, password=None):
        """
        creates user based on the provided user_id,
        email, user_type and password
        :return:
        """
        properties = [user_id, email, type, password]
        for prop in properties:
            if not property:
                raise ValueError('User must have a {)'.format(prop))

        user = self.model(
            user_id=user_id,
            email=self.normalize_email(email),
            type=type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, email, type, password=None):
        """
        creates a superuser based on the provided user_id,
        email, user_type and password
        :return:
        """
        user = self.create_user(user_id=user_id, email=email, type=type, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

