import requests

from apps.tests.models import Test, Question, Option
from conf.celery import app
from bs4 import BeautifulSoup as bs


@app.task
def first() -> None:

    test = Test.objects.get(title='New')
    last_question = test.questions.last()

    last_question_site_id = int(last_question.title[0:last_question.title.find('.')]) \
        if last_question else 0

    url = 'https://centrevraz.ru/dlya-rvp-vnzh'
    response = requests.get(url)
    soup = bs(response.text, "html.parser")

    questions = soup.findAll('div', class_='test_t')
    if len(questions) != last_question_site_id:
        soup_question = questions[last_question_site_id].find('b').text
        soup_labels = questions[last_question_site_id].findAll('label')
        soup_options = [label.find('input').get('value') for label in soup_labels]

        q = Question.objects.create(
            test=test,
            title=soup_question
        )

        Option.objects.bulk_create([Option(
            question=q,
            title=option
        ) for option in soup_options])


# @app.task
# def first() -> None:
#
#     test = Test.objects.get(title='New')
#     last_question = test.questions.last()
#     if last_question:
#         last_question_site_id = int(last_question.title[0:last_question.title.find('.')])
#     else:
#         last_question_site_id = 0
#     url = 'https://centrevraz.ru/dlya-rvp-vnzh'
#
#     response = requests.get(url)
#     soup = bs(response.text, "html.parser")
#
#     questions = soup.findAll('div', class_='test_t')
#     if len(questions) == last_question_site_id:
#         return
#     question = questions[last_question_site_id].find('b').text
#     labels = questions[last_question_site_id].findAll('label')
#     options = [label.find('input').get('value') for label in labels]
#
#     q = Question.objects.create(
#         test=test,
#         title=question
#     )
#     for option in options:
#         Option.objects.create(
#             question=q,
#             title=option
#         )

