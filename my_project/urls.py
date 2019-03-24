from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import url

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url('auth/', include('social_django.urls', namespace='social')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
