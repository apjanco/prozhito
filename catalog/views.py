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
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'catalog/search.html', context)

def range(request):
    return render(request, 'catalog/divcontent.html')


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

def getPublicationByKeyword(request):
    template = "catalog/search_results.html"
    query = request.GET.get("keyword")
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

def getPublicationByAuthor(request):
    authors = Author.objects.all()
    template = "catalog/search_results.html"
    author_query = request.GET.get("author_name")
    start_year_query = request.GET.get("year_min")
    end_year_query = request.GET.get("year_max")
    if not (author_query==None):
        results = Publication.objects.filter(Q(year__lte=end_year_query, year__gte=start_year_query, author__last_name__icontains=author_query))
        num_publications = results.count()
        context = {
        'publications': results,
        'num_results': num_publications,
        'authors': authors
        }
#author__last_name__icontains=author_query and
        return render(request, template, context)
    else:
        context = {
        'publications': None,
        'num_results': 0,
        'authors': authors
        }
        return render(request, template, context)
