from django.contrib import admin

# Register your models here.
from catalog.models import *
from django.utils.html import format_html


"""
admin.site.register(Publication)
admin.site.register(Author)
admin.site.register(Edition)
"""
# Define the admin class

# Register the admin class using the decorator


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

# Register the Admin classes for Book using the decorator


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author', 'journal', 'text']
    list_filter= ['year','journal', 'issue']
    list_display= ['author','title','pub_url']

    def pub_url(self, obj):
        return format_html("<a target='_blank' href='{url}'>{url}</a>", url=obj.url)

    pub_url.short_description = "Firm URL"
    #autocomplete_fields = ['author','journal']
# Register the Admin classes for BookInstance using the decorator


@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_filter = ('journal', 'number', 'year')
    list_display = ('journal', 'number', 'year')


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    filter = ('name')

@admin.register(TableofContents)
class TableofContentsAdmin(admin.ModelAdmin):
    list_display = ('order','journal', 'year', 'issue', 'category', 'author', 'link','title','genre')
