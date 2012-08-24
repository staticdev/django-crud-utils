# -*- coding: utf-8 -*- 
from django import template

register = template.Library()

@register.filter
def shorten_name(obj):
	names_to_ignore = ["de", "do", "dos", "da", "das", "e"]
	name_tokens = obj.split()
	if len(name_tokens) <= 2:
		return obj
	else:
		abbreviated_names = ""
		for i in range(1, len(name_tokens)-1):
			if name_tokens[i] not in names_to_ignore:
				abbreviated_names += "%s. " % name_tokens[i][0]
		return "%s %s%s" % (name_tokens[0], abbreviated_names, name_tokens[len(name_tokens)-1])

@register.filter
def class_name(obj):
	return obj.__class__.__name__

@register.filter
def class_verbose_name(obj):
	return obj.__class__._meta.verbose_name

@register.filter
def form_verbose_name(obj):
	try:
		getattr(obj, 'verbose_name')
	except AttributeError:
		return obj._meta.model._meta.verbose_name.title()
	else:
		return obj.verbose_name.title()

@register.filter
def lower(value): # Only one argument.
	return value.lower()

@register.filter
def capitalize(value): # Only one argument.
	return value.capitalize()

@register.filter
def get_fields(self):
	# procura uma funcao no model de personalizacao dos campos exibidos
	try:
		fieldset = self.__class__.get_fieldlist(self)
	# se nao achar usa os todos os campos do model
	except:
		fieldset = self.__class__._meta.fields
		import sys
		print "Unexpected error:", sys.exc_info()[0]

	fields = []
	for field in fieldset:
		if (self._get_FIELD_display(field) == None or self._get_FIELD_display(field) == ''):
			fields.append((field.verbose_name, u"Não disponível"))
		else:
			if (field.__class__.__name__ == 'DateField'):
				fields.append((field.verbose_name, self._get_FIELD_display(field).strftime("%d/%m/%Y")))
			elif (field.__class__.__name__ == 'DateTimeField'):
				fields.append((field.verbose_name, self._get_FIELD_display(field).strftime("%d/%m/%Y")))
			else:
				fields.append((field.verbose_name, self._get_FIELD_display(field)))
	return fields

### TESTING ###
@register.filter
def stringfy(obj):
	return str(obj)

@register.filter
def get_first_fields(self):
	fields=[]
	try:
		fieldset = self.__class__.FIELDSETS_COMMON[0][1]['fields']
		fields = [self.__class__._meta.get_field_by_name(i)[0] for i in fieldset]
	except:
		fields = self.__class__._meta.fields
		print "Warning: " + self.__class__.__name__ + " doesn't have FIELDSETS_COMMON attribute. Using all fields instead. If you are using Django builtin models, it is recommended to use proxy models."
		# Doesnt show ID field
		fields = fields[1:]
	return fields

@register.filter
def get_first_field_values(self):
	fieldset = []
	try:
		fieldnameset = self.__class__.FIELDSETS_COMMON[0][1]['fields']
		for fieldname in fieldnameset:
			field = self.__class__._meta.get_field_by_name(fieldname)[0]
			fieldset.append(field)
	except:
		# Doesnt have to emit warning for each instance, get_first_fields() print this warning once.
		for field in self.__class__._meta.fields:
			fieldset.append(field)
		# Doesnt show ID field
		fieldset = fieldset[1:]
	fieldvalues=[]
	for field in fieldset:
		if (self._get_FIELD_display(field) == None or self._get_FIELD_display(field) == ''):
			fieldvalues.append(u"Não disponível")
		else:
			if (field.__class__.__name__ == 'DateField'):
				fieldvalues.append(self._get_FIELD_display(field).strftime("%d/%m/%Y"))
			elif (field.__class__.__name__ == 'DateTimeField'):
				fieldvalues.append(self._get_FIELD_display(field).strftime("%d/%m/%Y"))
			else:
				fieldvalues.append(self._get_FIELD_display(field))
	return fieldvalues