from django.shortcuts import render

from django.views import generic

# Create your views here.
from catalog.models import Publication, Author, Journal, Edition

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_publications = Publication.objects.all().count()


    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_journals = Journal.objects.count()
    context = {
        'num_publications': num_publications,
        'num_authors': num_authors,
        'num_journals': num_journals,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class PublicationListView(generic.ListView):
    model = Publication

class PublicationDetailView(generic.DetailView):
    model = Publication

class JournalListView(generic.ListView):
    model = Journal

class JournalDetailView(generic.DetailView):
    model = Journal
