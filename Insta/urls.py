from django.urls import path
from . import views

urlpatterns = [
    path('', views.HelloDjango.as_view())
]