from django.contrib import admin
from django.urls import path, include

from apps.api import urls as api_urls
from apps.accounts import urls as account_urls


urlpatterns = [
    path('', include(api_urls)),
    path('', include(account_urls)),
    path('nested_admin/', include('nested_admin.urls')),
    path('admin/', admin.site.urls),
]
