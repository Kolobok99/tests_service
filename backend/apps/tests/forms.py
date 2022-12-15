from django import forms
from django.core.exceptions import ValidationError

from . import models


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = "__all__"


class OptionForm(forms.ModelForm):
    class Meta:
        model = models.Option
        fields = "__all__"


class OptionInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):

        right_count = 0
        for form in self.forms:
            if form.cleaned_data['is_right']:
                right_count +=1

        if len(self.forms) == 1:
            raise ValidationError('Ошибка: должно быть хотя бы два варианта ответа!')
        elif right_count == 0:
            raise ValidationError('Ошибка: должен быть хотя бы один верный ответ!')
        elif right_count == len(self.forms):
            raise ValidationError('Ошибка: все ответы не могут быть правильными!')

