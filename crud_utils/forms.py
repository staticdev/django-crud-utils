from django import forms
from django.utils.translation import ugettext as _

class SearchForm(forms.Form):
	search		=	forms.CharField(label=_('Nome'), max_length=200, required=False)
