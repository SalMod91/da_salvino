from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Create and save a regular user with the given username and password.
        """
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
    Custom User model for Staff that replaces the default Django user model.

    This model uses a username for authentication instead of an email address
    and includes additional fields like staff, admin, and is_approved flags.
    """

    # Username field with a maximum length of 15 characters, must be unique
    username = models.CharField(
        max_length=15,
        unique=True,
    )
    # Boolean fields to determine if a user is staff, admin, or approved
    staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    # Specify the field used for logging in
    USERNAME_FIELD = 'username'

    # Custom manager for creating users and superusers
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
