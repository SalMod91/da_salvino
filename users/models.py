from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """Create and save a regular user with the given username and password."""
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """Create and save a superuser with the given username and password."""
        user = self.create_user(username, password)
        user.staff = True
        user.admin = True
        user.is_approved = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomStaffUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom User for Staff
    """
    username = models.CharField(
        max_length=15,
        unique=True,
    )
    staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    class Meta:
        verbose_name = "Staff User"
        verbose_name_plural = "Staff Users"

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user an admin member?"
        return self.admin
