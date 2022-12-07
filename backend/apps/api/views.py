from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.accounts import forms as accounts_forms



class RegistrationView(CreateView):
    """
        Контроллер: Регистрация пользователя
    """

    template_name = 'registration.html'
    form_class = accounts_forms.UserCreateForm
    success_url = reverse_lazy('main-page')

