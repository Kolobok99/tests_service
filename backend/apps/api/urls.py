from django.urls import path
from rest_framework import routers

from apps.api import views

urlpatterns = [
    path('question/<int:id>/', views.GetTrueOptionsByQuestionId.as_view())
]