from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from crud_utils.forms import SearchForm

class CrudUtilsDetailView(DetailView):
	template_name='generic_detail.html'

class CrudUtilsCreateView(CreateView):
	template_name='generic_insert.html'

class CrudUtilsUpdateView(UpdateView):
	template_name='generic_insert.html'

class CrudUtilsDeleteView(DeleteView):
	template_name='generic_delete.html'

	"""

    Returns a nested list of strings suitable for display in the
    template with the ``unordered_list`` filter. Inspired on django.contrib.admin.util function.

    """
	def get_deleted_objects(objs):
		from django.contrib.admin.util import NestedObjects
		collector = NestedObjects(using='default') # or specific database
#		collector = NestedObjects(using=using)
		collector.collect(objs)

		return collector.nested()

	def get_context_data(self, **kwargs):
		context = super(self.__class__, self).get_context_data(**kwargs)
		context['deleted_objects'] = self.get_deleted_objects([context['object']])

		return context

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