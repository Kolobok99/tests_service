from django.db import models


class BaseModel(models.Model):
    """Базовая модель"""

    objects = models.Manager()

    created_on = models.DateTimeField('Время создания ', auto_now_add=True)
    modified_on = models.DateTimeField('Время добавления', auto_now=True)

    def get_model_fields(self):
        return self._meta.fields

    class Meta:
        abstract = True


