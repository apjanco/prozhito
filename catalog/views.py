from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import generic



# Create your views here.
from catalog.models import Publication, Author, Journal, Edition
from catalog.forms import AuthorAutocompleteForm

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_publications = Publication.objects.count()


    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_journals = Journal.objects.count()
    context = {
        'num_publications': num_publications,
        'num_authors': num_authors,
        'num_journals': num_journals,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)

def search(request):
    return render(request, 'catalog/search.html')

def search_results(request):
    context={
        'publications': ["1", "2"]
        }
    return render(request, "catalog/search_results.html", context)

class PublicationListView(generic.ListView):
    model = Publication

class PublicationDetailView(generic.DetailView):
    model = Publication

class JournalListView(generic.ListView):
    model = Journal

class JournalDetailView(generic.DetailView):
    model = Journal

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

def getPublicationByAuthor(request):
    template = "catalog/search_results.html"
    query = request.GET.get("author_name")
    if not query==None:
        results = Publication.objects.filter(Q(title__icontains=query))
        num_publications = results.count()
        context = {
        'publications': results,
        'num_results': num_publications,
        }

        return render(request, template, context)
    else:
        return render(request, template, context=None)
