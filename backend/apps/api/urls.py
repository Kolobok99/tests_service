from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('test/<int:pk>/', views.TestRetrieveView.as_view(), name='test-detail'),
    path('test/<int:pk>/start/', views.StartNewTest.as_view(), name='test-start'),
    path('test/<int:test_pk>/questions/', views.QuestionView.as_view(), name='question-detail'),
    path('test/create/', views.TestCreate.as_view(), name='test-create'),
]
