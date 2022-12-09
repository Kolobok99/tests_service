from django import forms
from django.core.exceptions import ValidationError

from . import models

class TestCreateForm(forms.ModelForm):

    class Meta:
        model = models.Test
        fields = "__all__"