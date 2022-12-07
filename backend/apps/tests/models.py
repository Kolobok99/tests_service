from django.db import models
from django.urls import reverse_lazy

from apps.base.models import BaseModel


class Test(BaseModel):
    """Модель теста"""

    title = models.CharField("Название", max_length=32)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('test-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(BaseModel):
    """Модель вопроса"""

    title = models.CharField('Вопрос', max_length=128)

    test = models.ForeignKey("Test", on_delete=models.CASCADE, related_name='questions')

    # selected_option = models.ForeignKey('Option', on_delete=models.PROTECT,
    #                                     related_name='temporary_name',
    #                                     null=True, blank=True, editable=False)

    def __str__(self):
        return f"ТЕСТ [{self.test}] {self.title}"

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Option(BaseModel):
    """Модель Вариант ответа"""

    title = models.CharField("Заголовок", max_length=256)
    is_right = models.BooleanField("Правильный?", default=False)

    question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return f"{self.question}_{self.title}_{self.is_right}"

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'


