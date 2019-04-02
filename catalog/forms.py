from django.forms import ModelForm

from catalog.models import Publication

class AuthorAutocompleteForm(ModelForm):

    def clean_author(self):
       data = self.cleaned_data['due_back']

       # Check if author field is a string of letters
       if not data.isalpha():
           raise ValidationError(_('Invalid author name - only letters allowed'))


       return data

    class Meta:
        model = Publication
        fields = ['author']
        labels = {'author': ("Author's name")}
        help_texts = {'author': ('Enter a name of an author. Only letters allowed')}
