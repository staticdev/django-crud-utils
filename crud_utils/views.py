from django.contrib.admin.util import get_deleted_objects
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
#from django.contrib.auth.decorators import login_required

from crud_utils.forms import SearchForm

class CrudUtilsDetailView(DetailView):
	template_name='generic_detail.html'

class CrudUtilsCreateView(CreateView):
	template_name='generic_insert.html'

class CrudUtilsUpdateView(UpdateView):
	template_name='generic_insert.html'

class CrudUtilsDeleteView(DeleteView):
	template_name='generic_delete.html'

## TO-DO: colocar lista de objetos deletados
#	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
#		context = super(self.__class__, self).get_context_data(**kwargs)

#		opts = self.model._meta
		# Populate deleted_objects, a data structure of all related objects that
		# will also be deleted.
#		(context['deleted_objects'], context['perms_needed'], context['protected']) = get_deleted_objects(
#			[obj], opts, request.user, self.admin_site, using)

class CrudUtilsListView(ListView):
	template_name='generic_list.html'
	custom_name=None
	custom_name_plural=None

	def get_form_kwargs(self):
		self.can_see_page()
		kwargs = super(CrudUtilsListView, self).get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(self.__class__, self).get_context_data(**kwargs)

		# Sets the name shown in the template
		if self.custom_name == None:
			context['auto_name'] = self.model._meta.verbose_name.title()
		else:
			context['auto_name'] = self.custom_name
		if self.custom_name_plural == None:
			if self.custom_name == None:
				context['auto_name_plural'] = self.model._meta.verbose_name_plural.title()
			else:
				context['auto_name_plural'] = self.custom_name + "s"
		else:
			context['auto_name_plural'] = self.custom_name_plural

		# Adiciona form de search no template		
		if self.request.method == "GET" and "submit_search" in self.request.GET:
			context['form'] = SearchForm(self.request.GET)
			term = self.request.GET.get('search', '')

			if context['form'].is_valid():
				if "search" in self.request.GET:
					context['object_list'] = context['object_list'].filter(name__icontains=term)

# TO-DO: Melhorar buscar para procurar em varios campos - ver heystack e solr
#					fields = [f for f in ._meta.fields if isinstance(f, CharField)]
#					queries = [Q(**{f.name: term}) for f in fields]
#
#					qs = Q()
#					for query in queries:
#						qs = qs | query
#
#					context['object_list'] = context['object_list'].filter(qs)

		else:
			context['form'] = SearchForm()
		# ordena por name
		context['object_list'] = context['object_list'].order_by('name')
		return context