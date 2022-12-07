from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView
from rest_framework.response import Response

from apps.tests import models as tests_models
from apps.accounts import models as accounts_models

class MainView(TemplateView):

    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tests'] = tests_models.Test.objects.all()
        return context

class TestRetrieveView(DetailView):

    template_name = 'test_retrieve.html'
    model = tests_models.Test


def start_new_test(request):
    print(1)
    # if request.GET:
    #     user = request.user
    #     test_pk = request.GET.get('pk')
    #     print(f"{user=}")
    #     print(f"{test_pk=}")


class StartNewTest(View):

    def get(self, request, pk):
        user = request.user
        print(f"{user.email=}")

        test = tests_models.Test.objects.get(pk=pk)
        solved_user_test = accounts_models.SolvedTest.objects.filter(
            Q(test=test) and Q(user=user) and Q(status='C')
        )
        if solved_user_test:
            return Response({"message": "Завершите прошлый тест!"})
        new_solved_test = accounts_models.SolvedTest.objects.create(
            user=user,
            test=test
        )
        first_question = test.questions.first()
        return HttpResponseRedirect(
            reverse_lazy('question-detail',
                         kwargs={'test_pk': test.pk, 'question_pk': first_question.pk}
                         )
        )


class QuestionView(DetailView):

    template_name = 'question_detail.html'
    model = tests_models.Question
    pk_url_kwarg = 'question_pk'
