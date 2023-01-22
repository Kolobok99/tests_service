from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView

from apps.tests import models as tests_models
from apps.accounts import models as accounts_models


from django.contrib.auth.mixins import LoginRequiredMixin


class MainView(LoginRequiredMixin, TemplateView):
    """
        Контроллер: главной страницы
        Функционал:
                    вывод:
                          список тестов
    """

    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        """
            Возвращает контекст:
                test - все тесты
        """

        context = super().get_context_data(**kwargs)
        context['tests'] = tests_models.Test.objects.all()
        return context


class TestRetrieveView(LoginRequiredMixin, DetailView):
    """
    Контроллер: тест по test_id
    Функционал:
              начать/продолжить выполнение теста
              вывод результатов прохождениев теста
    """

    template_name = 'test_retrieve.html'
    model = tests_models.Test

    def get_context_data(self, **kwargs):
        """
            Возвращает контекст:
                finished_tests - все завершенные тесты,
                                выбранного теста user'a
        """
        context = super().get_context_data(**kwargs)
        context['finished_tests'] = accounts_models.SolvedTest.objects.filter(
            user=self.request.user,
            test=self.get_object(),
            status='F'
        )

        return context


class StartNewTest(LoginRequiredMixin, View):
    """
        Контроллер: генерирует новый SolvedTest для текущего user'а

    """

    def get(self, request, pk):
        """

        """

        user = request.user
        test = tests_models.Test.objects.get(pk=pk)

        # Возвращает все незаконченные тесты
        solved_user_test = accounts_models.SolvedTest.objects.filter(
            Q(test=test) and Q(user=user) and Q(status='C')
        )

        # Если тест незавершен, перенаправляет на последний, неотвеченный вопрос
        if solved_user_test:
            return HttpResponseRedirect(
                reverse_lazy('question-detail',
                             kwargs={'test_pk': test.pk}
                             )
            )
        # Иначе генерирует новый Тест и вопросы к нему
        new_solved_test = accounts_models.SolvedTest.objects.create(
            user=user,
            test=test
        )
        test_questions = test.questions.all()

        for q in test_questions:
            accounts_models.SolvedQuestion.objects.create(
                solved_test=new_solved_test,
                question=q,
            )

        return HttpResponseRedirect(
            reverse_lazy('question-detail',
                         kwargs={'test_pk': test.pk}
                         )
        )


class QuestionView(LoginRequiredMixin, DetailView):
    """
        Контроллер: генерирует стр. последнего
                    неотвеченный вопрос теста
        Функционал:
                    выводит вопрос и варианты ответов
                    с возможностью отправки ответов
    """

    template_name = 'question_detail.html'
    model = accounts_models.SolvedQuestion

    def post(self, request, test_pk):
        """Сохраняет ответы текущего вопроса"""

        solved_question = self.get_object()
        solved_test = solved_question.solved_test

        # Добавляем выбранные ответы к вопросу
        options = tests_models.Option.objects.filter(pk__in=request.POST.getlist('options'))
        solved_question.responses.add(*options)

        # Если остались неотвеченные вопросы, редирект на следующий вопрос
        questions_with_out_responses = accounts_models.SolvedQuestion.objects.filter(
            solved_test=solved_test,
            responses__isnull=True
        )

        if questions_with_out_responses:
            return HttpResponseRedirect(self.request.path_info)

        # Иначе вычисляем кол-во правильных и неправильных ответов

        solved_questions = solved_test.solved_questions.all()
        corrects = solved_questions.exclude(responses__is_right=False).count()

        solved_test.corrects = corrects
        solved_test.un_corrects = solved_questions.count() - corrects
        solved_test.status = 'F'
        solved_test.save()

        # и редирект на стр. теста
        return HttpResponseRedirect(solved_test.test.get_absolute_url())

    def get_object(self, queryset=None, **kwargs):
        """
            Возвращает первый вопрос теста
            у которго нет ответов (responses__isnull=True)
        """
        user = self.request.user

        # Возрващает test_id из path (/test/1/questions/)
        test_pk = self.request.path.split('/')[2]

        test = accounts_models.SolvedTest.objects.get(test_id=test_pk, status='C')
        questions = accounts_models.SolvedQuestion.objects.filter(
            solved_test=test,
            responses__isnull=True
        )

        return questions.first()
