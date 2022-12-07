from django.db import models

from apps.base.models import BaseModel


class Test(BaseModel):
    """Модель теста"""

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(BaseModel):
    """Модель вопроса"""

    test = models.ForeignKey("Test", on_delete=models.CASCADE, related_name='questions')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Option(BaseModel):
    """Модель Вариант ответа"""
    #
    # def get_serial(self):
    #     number = Test.objects.get(que)

    title = models.CharField("Заголовок", max_length=256)
    is_right = models.BooleanField("Правильный?", default=False)

    question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name='options')
    # serial = models.PositiveIntegerField("Порядковый номер", default=)
    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'


