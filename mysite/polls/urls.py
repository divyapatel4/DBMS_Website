from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('form', views.form, name='form'),
    path('results', views.results, name='results'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)