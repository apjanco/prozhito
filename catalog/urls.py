from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('publications/', views.PublicationListView.as_view(), name='publications'),
    path('publication/<int:pk>', views.PublicationDetailView.as_view(), name='publication-detail'),
    path('journals/', views.JournalListView.as_view(), name='journals'),
    path('journal/<int:pk>', views.JournalDetailView.as_view(), name='journal-detail'),
    path('search/', views.getPublicationByAuthor, name='search'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('range/', views.range, name="range"),
    # path('search_results/', views.PublicationListView.as_view(), name='publications'),
]
