from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from apps.base.models import BaseModel
from apps.tests.models import Test


class UserManager(BaseUserManager):
    """
        Менеджер: модели MyUser
    """

    def create_user(self, email, password, **extra_fields):
        """ Создание user'а """
        if not email:
            raise ValueError("Укажите Email!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        """Создание root'а """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'a')

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Root должен иметь is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Root должен иметь is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class UserModel(BaseModel, AbstractBaseUser, PermissionsMixin):
    """ Модель: Пользователь """


    email = models.EmailField('Почта', unique=True,
                              error_messages={
                                  'unique': 'Пользователь с таким email уже существует.',
                                  'invalid': 'Некорректный email'
                              })
    password = models.CharField("Пароль", max_length=128)
    is_active = models.BooleanField("Активирован?", default=True, editable=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects = UserManager()

    # заглушка для избежания ошибок переопределения AbstractBaseUser
    last_login = None

    def update_last_login(sender, user, **kwargs):
        pass

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class SolvedTest(BaseModel):
    """Экземпляр теста решаемого Пользователем"""

    user = models.ForeignKey("UserModel", on_delete=models.CASCADE, related_name='my_tests')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='solved_tests')

