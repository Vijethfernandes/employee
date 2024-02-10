from django.urls import path
from emp_app import views

urlpatterns = [
    path('', views.add_emp, name='add_emp'),
]