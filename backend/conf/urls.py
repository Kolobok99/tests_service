from django.contrib import admin
from django.urls import path, include

from apps.api import urls as main_urls

urlpatterns = [
    path('', include(main_urls)),
    path('admin/', admin.site.urls),
]
