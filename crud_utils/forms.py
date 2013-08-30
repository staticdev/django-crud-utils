#change in forms to use floppyforms widgets
import floppyforms as forms
from django.utils.translation import ugettext as _


class SearchForm(forms.Form):
    search = forms.CharField(label=_('Nome'), widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=200, required=False)
