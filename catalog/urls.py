from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('publications/', views.PublicationListView.as_view(), name='publications'),
    path('publication/<int:pk>', views.PublicationDetailView.as_view(), name='publication-detail'),
]
