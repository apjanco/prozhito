# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import generic
import csv
from django.http import HttpResponse
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from catalog.models import Entries
from django.utils.html import escape, format_html, mark_safe
from django_markup.markup import formatter
from django.core import serializers

# Create your views here.

def index(request):

    return render(request, 'catalog/index.html',)

def entries_text(request, query):

    args = request.GET.get('q', '')
    entries = Entries.objects.filter(text__icontains=query)
    text = ''.join([entry.text for entry in entries])

    return HttpResponse(args + text)

def entries_json(request, query):

    entries = Entries.objects.filter(text__icontains=query)

    data = serializers.serialize('json', entries)
    return HttpResponse(data, content_type='application/json')

class DiariesJson(BaseDatatableView):
    # the model you're going to show
    model = Entries

    """text = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    datetop = models.CharField(max_length=220, blank=True, null=True)
    firstname = models.CharField(max_length=220, blank=True, null=True)
    lastname = models.CharField(max_length=220, blank=True, null=True)
    thirdname = models.CharField(max_length=220, blank=True, null=True)
    nickname = models.CharField(max_length=220, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    birthday = models.CharField(max_length=220, blank=True, null=True)
    deathday = models.CharField(max_length=220, blank=True, null=True)
    wikilink = models.TextField(blank=True, null=True)"""

    # define columns that will be returned
    # they should be the fields of your model, and you may customize their displaying contents in render_column()
    # don't worry if your headers are not the same as your field names, you will define the headers in your template
    columns = ['text', 'date', 'firstname', 'thirdname', 'lastname',]# 'info', 'birthday', 'deathday', 'wikilink']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns displayed by datatables
    # for non sortable columns use empty value like ''
    order_columns =  ['text', 'date','firstname', 'thirdname', 'lastname',]# 'info', 'birthday', 'deathday', 'wikilink']

    # set max limit of records returned
    # this is used to protect your site if someone tries to attack your site and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        # we want to render 'translation' as a custom column, because 'translation' is defined as a Textfield in Image model,
        # but here we only want to check the status of translating process.
        # so, if 'translation' is empty, i.e. no one enters any information in 'translation', we display 'waiting';
        # otherwise, we display 'processing'.
        if column == 'text':
            return format_html("<p>{}</p>".format(formatter(row.text, filter_name='markdown')))
        if column == 'date':
            return format_html("<p>{}</p>".format(row.date,))
        if column == 'firstname':
            return format_html("<p>{}</p>".format(row.firstname,))
        if column == 'lastname':
            return format_html("<p>{}</p>".format(row.lastname,))
        if column == 'thirdname':
            return format_html("<p>{}</p>".format(row.thirdname,))
        if column == 'nickname':
            return format_html("<p>{}</p>".format(row.nickname,))
        if column == 'gender':
            return format_html("<p>{}</p>".format(row.gender,))

        else:
            return super(DiariesJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # here is a simple example
        search = self.request.GET.get('search[value]', None)
        if search:
            q = Q(text__icontains=search) | Q(date__icontains=search) | Q(firstname__icontains=search) | Q(lastname__icontains=search)
            qs = qs.filter(q)
        return qs
