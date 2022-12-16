from django.contrib import admin
from django.urls import path, include

from apps.tests import urls as tests_urls
from apps.accounts import urls as account_urls


urlpatterns = [
    path('', include(tests_urls)),
    path('', include(account_urls)),
    path('nested_admin/', include('nested_admin.urls')),
    path('admin/', admin.site.urls),
]
