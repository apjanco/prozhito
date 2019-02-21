from django.db import models

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Journal(models.Model):
    """Model representing a journal."""
    name = models.CharField(max_length=200, help_text='Enter a journal name (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Author(models.Model):
    "Model representing the author of an article"

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


class Article(models.Model):
    """Model representing an article (but not a specific copy of an article)."""
    title = models.CharField(max_length=200)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    text = models.TextField(help_text='Text of the article')
    date = models.DateField(auto_now_add = True, help_text='Date when article was published')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    journal = models.ManyToManyField(Journal, help_text='Journal in which the article is published')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('article-detail', args=[str(self.id)])

# Create your models here.
