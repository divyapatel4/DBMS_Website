from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('form', views.form, name='form'),
    path('get_args', views.get_args, name='get_args'),
    path('results', views.results, name='results'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)