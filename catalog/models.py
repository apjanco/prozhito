from django.db import models

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.html import format_html
import datetime
import uuid

class Journal(models.Model):
    """Model representing a journal."""
    name = models.CharField(max_length=200, help_text='Enter a journal name (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this journal."""
        return reverse('journal-detail', args=[str(self.id)])

class Author(models.Model):
    "Model representing the author of an publication"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.last_name

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Edition(models.Model):
    """Model representing an edition of a journal"""

    number = models.IntegerField(help_text='Number of the edition')
    year = models.IntegerField(help_text='Year of the edition', validators=[MinValueValidator(0),
                                       MaxValueValidator(datetime.date.today().year+1)])
    journal = models.ForeignKey(Journal, on_delete=models.SET_NULL, null=True, related_name="journal")

    def __str__(self):
        """String for representing the Model object."""
        return (str(self.journal) + ", " + str(self.year) + ", " + str(self.number) + " edition")

class Publication(models.Model):

    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular publication')
    title = models.TextField(help_text='Text of the publication', blank=True,)
    author = models.CharField(max_length=200, blank=True,)
    journal = models.CharField(max_length=200, blank=True,)
    text = models.TextField(help_text='Text of the publication', blank=True,)
    year = models.IntegerField(null=True, blank=True, default=None,)
    issue = models.IntegerField(null=True, blank=True, default=None,)
    url = models.TextField(help_text='Text of the publication', blank=True,)
    #is_translation = Binary
    #translator =
    #From TOC
    #order in toc
    #genre <i>
    #category in toc <h6>

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this publication."""
        return format_html(u'<a target="_blank" href="{}">{}</a>'.format(self.url, self.url))

class TableofContents(models.Model):
    order = models.IntegerField(null=True, blank=True, default=None)
    journal = models.CharField(max_length=200, blank=True,)
    year = models.IntegerField(null=True, blank=True, default=None)
    issue = models.IntegerField(null=True, blank=True, default=None)
    category = models.CharField(max_length=200, blank=True,null=True,)
    author = models.CharField(max_length=200, blank=True,null=True,)
    link = models.CharField(max_length=200, blank=True,null=True,)
    title = models.TextField(help_text='Text of the publication', blank=True,null=True,)
    genre = models.TextField(help_text='Text of the publication', blank=True,null=True,)
    text= models.TextField(help_text='Text of the publication', blank=True,null=True,)


