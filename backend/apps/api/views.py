from django.views.generic import TemplateView, DetailView

from apps.tests import models as tests_models

class MainView(TemplateView):

    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tests'] = tests_models.Test.objects.all()
        return context

class TestRetrieveView(DetailView):

    template_name = 'test_retrieve.html'
    model = tests_models.Test
