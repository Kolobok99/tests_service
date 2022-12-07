from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps.api import views


urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login.html', next_page='login'), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]
