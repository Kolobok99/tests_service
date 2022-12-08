from django import forms
from django.core.exceptions import ValidationError

from . import models

class UserCreateForm(forms.ModelForm):
    """
        Форма: регистрация пользователя
    """

    password_repeat = forms.CharField(label='Повторите пароль',
                                      widget=forms.widgets.PasswordInput()
                                      )

    def save(self, **kwargs):
        self.instance.set_password(self.cleaned_data['password'])
        return super().save(**kwargs)

    def clean(self):
        cleaned_data = super().clean()
        errors = {}

        pass1 = cleaned_data.get('password')
        pass2 = cleaned_data.get('password_repeat')

        if pass1 != pass2:
            errors['password_repeat'] = 'Пароли не совпадают!'

        if errors:
            raise ValidationError(errors)
        else:
            return cleaned_data

    class Meta:
        model = models.UserModel
        fields = (
            'email',
            'password',
            'password_repeat',
        )
