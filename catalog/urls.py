from django.urls import path
from . import views
from django.views.generic import TemplateView
from catalog.views import DiariesJson

urlpatterns = [
    path('', views.index, name='index'),
    
]
