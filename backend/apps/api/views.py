from rest_framework.response import Response
from rest_framework.views import APIView

from apps.tests.models import Option


class GetTrueOptionsByQuestionId(APIView):
    def get(self, request, id=None):
        """
        Возвращает список правильный ответов вопроса

        Args:
            id (int) - ID вопроса
        Return:
              [id] - список id правильных ответов
        """
        true_options = Option.objects.filter(question_id=id, is_right=True).only('id')
        return Response([x.id for x in true_options])



