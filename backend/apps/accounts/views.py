from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms


class RegistrationView(CreateView):
    """
        Контроллер: Регистрация пользователя
    """

    template_name = 'registration.html'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')