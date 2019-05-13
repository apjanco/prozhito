from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import generic
import csv
from django.http import HttpResponse


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

class EditionListView(generic.ListView):
    model = Edition

class EditionDetailView(generic.DetailView):
    model = Edition

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
    authors = Author.objects.all().order_by("last_name")
    template = "catalog/search_results.html"
    author_query = request.GET.get("author_name")
    start_year_query = request.GET.get("startYear")
    end_year_query = request.GET.get("endYear")
    year = request.GET.get("startYear")
    if not (author_query==None):
        results = Publication.objects.filter(Q(year__lte=end_year_query, year__gte=start_year_query, author__last_name__icontains=author_query))
        num_publications = results.count()
        context = {
        'publications': results,
        'num_results': num_publications,
        'authors': authors,
        'year': year,
        }
#author__last_name__icontains=author_query and
        return render(request, template, context)
    else:
        context = {
        'publications': None,
        'num_results': 0,
        'authors': authors,
        'year': year,
        }
        return render(request, template, context)


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Publication-Disposition'] = 'attachment; filename="search_results.csv"'
    #figure out how to get values from html to here
    #run the query again
    #write a temp file in memory with the search results so that user can download it
    #NamedTemporaryFile() - write the result to that file as a csv, pass that to a template
    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response


def getPublicationByAuthor2(request):
    authors = Author.objects.all()
    template = "catalog/search_results.html"
    author_query = request.GET.get("author_name")
    start_year_query = request.GET.get("year_min")
    end_year_query = request.GET.get("year_max")

    if start_year_query==None:      #if no start year was input, set default to zero
        start_year_query = 0
    if end_year_query==None:        #if no end year was input, set default to the most current year
        end_year_query = datetime.date.now().year
    if author_query==None:          #if no author was input, set author query to empty string to include all authors
        author_query = ""

    results = Publication.objects.filter(Q(year__lte=end_year_query, year__gte=start_year_query, author__last_name__icontains=author_query))
    context={
    'publications': results,
    'num_results': results.count(),
    'authors': authors
    }

    return render(request, template, context)
