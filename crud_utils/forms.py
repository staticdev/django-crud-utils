from django import forms
from django.utils.translation import ugettext as _

class SearchForm(forms.Form):
	search		=	forms.CharField(label=_('Nome'), widget=forms.TextInput(attrs={'class': 'input-medium search-query'}), max_length=200, required=False)
