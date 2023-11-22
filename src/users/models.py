from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_author = models.BooleanField(default=False)
    name = models.CharField(max_length=255, blank=True)
    profile_pic = models.ImageField(blank=True, upload_to="media/profile_pics/%Y/%m/%d/%H/%M")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )
    objects = CustomUserManager()

    def __str__(self):
        return self.email