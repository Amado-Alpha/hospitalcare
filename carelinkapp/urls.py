from django.urls import path
from django.views.generic import TemplateView
from .views import example_view

urlpatterns = [
    path('', example_view, name='homepage'),
]