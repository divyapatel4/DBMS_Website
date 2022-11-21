from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

app_name = 'polls'

admin.site.header = "Wildlife Sanctuary Database Management System"
admin.site.site_title = "Wildlife Sanctuary Database Management System"
admin.site.index_title = "Welcome to Wildlife Sanctuary Database Management System"
admin.site.site_header = "Wildlife Sanctuary Database Management System"

# Display app name in admin site


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('form', views.form, name='form'),
    path('results', views.results, name='results'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)