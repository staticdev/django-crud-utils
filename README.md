django-crud-utils
===============

An extension to the Django web framework that helps the development of model/view/templates for CRUD operations.

Setup
-----

Assuming you have django installed, you'll have to make the following modifcations to your `settings.py` file.

### Basic Settings ###

Install Django Crud Utils with your favorite Python package manager:

    pip install -e git://github.com/staticdev/django-crud-utils.git#egg=django-crud-utils

Don't forget to add `crud-utils` to your `INSTALLED_APPS`.
    
    INSTALLED_APPS = (
        ...
	    'crud-utils',
	    ...
	)
    
### Dependencies ###

For correct usage of this app, you need to install the following dependencies:

*   [django-pagination][]
Used for listing the objects of a class.
[django-pagination]: http://pypi.python.org/pypi/django-pagination
	"django-pagination"
    pip install django-pagination

*   [django-sorting][]
Used for sorting fields of a list.
[django-sorting]: https://github.com/staticdev/django-sorting
	"django-sorting"
    pip install -e git://github.com/staticdev/django-sorting.git#egg=django-sorting

Final Notes
-----
This app is in alpha version, this doc needs to be updated.
========================