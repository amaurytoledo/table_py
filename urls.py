from django.urls import path

from . import views

app_name = 'table_py'

urlpatterns = [
    path('admin/', views.admin, name='admin'),
]
