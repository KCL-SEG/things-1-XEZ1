from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator

class User(AbstractUser):
    username = models.CharField(
    max_length=30,
    unique=True,
    validators=[RegexValidator(
        regex=r'^@\w{3,}$',
        message='Username must consist of @ symbol followed by at least 3 alphanumericals'
        )]
    )

    first_name = models.CharField(
    max_length=50,
    blank=False,
    null=False,
    unique=False
    )

    last_name = models.CharField(
    max_length=50,
    blank=False,
    null=False,
    unique=False
    )

    email = models.EmailField(
    unique=True,
    blank=False
    )

    bio = models.CharField(
    max_length=520,
    blank=True
    )


class Thing(models.Model):
    name = models.CharField(
    max_length = 30,
    unique = True,
    blank = False
    )

    description = models.CharField(
    max_length = 120,
    unique = False,
    blank = True
    )

    quantity = models.IntegerField(
    unique = False,
    validators=[MaxValueValidator(100),
    MinValueValidator(0)]
    )
