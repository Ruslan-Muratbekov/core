from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.
class BaseAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')

        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, BaseAbstractModel, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name='Почта')
    first_name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Имя')
    last_name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Фамилия')

    is_staff = models.BooleanField(default=True, verbose_name='статус персонала')
    is_active = models.BooleanField(default=True, verbose_name='активность')
    is_superuser = models.BooleanField(default=False, verbose_name='cтатус администратора')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name_plural = 'Пользователь'
        verbose_name = 'Пользователь'
        ordering = ['first_name', 'last_name']
