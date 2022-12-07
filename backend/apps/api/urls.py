from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('test/<int:pk>/', views.TestRetrieveView.as_view(), name='test-detail')
]
