from django.contrib import admin

# Register your models here.
from catalog.models import Journal, Publication, Author, Edition



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
    list_display = ('title', 'author', 'edition')

# Register the Admin classes for BookInstance using the decorator
@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_filter = ('journal', 'number', 'year')
    list_display = ('journal', 'number', 'year')

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    filter = ('name')
