django-crud-utils
===============

An extension to the Django web framework that helps the development of model/view/templates for CRUD operations.

Setup
-----

Assuming you have django installed, you'll have to make the following modifcations to your `settings.py` file.

Installation
------------
To install ``django-crud-utils`` simply run::

    pip install -e git://github.com/staticdev/django-crud-utils.git#egg=django-crud-utils

Configuration
-------------

Don't forget to add `crud-utils` to your `INSTALLED_APPS`::

      INSTALLED_APPS = (
         ...
         'floppyforms',
         'pagination_bootstrap',
         'sorting_bootstrap',
         'crud_utils',
      )


Django Crud Utils requires a file called `base.html` in your template dirs from which will be extended all of its own templates.

Dependencies
-------------

For correct usage of this app, you need to install the following dependencies:

* `django-floppyforms`_: Used for HTML5 rendering of forms in the Create/Update templates. Install with::

    pip install -U django-floppyforms

* `django-pagination-bootstrap`_: Uses Twitter's Bootstrap Pagination of objects of a class. Install with::

    pip install django-bootstrap-pagination

* `django-sorting-bootstrap`_: Used for sorting fields of a list. Install with::

    pip install django-sorting-bootstrap

Final Notes
-------------

This app is in alpha version, this doc needs to be updated.

.. _django-floppyforms: https://pypi.python.org/pypi/django-floppyforms
.. _django-pagination-bootstrap: http://pypi.python.org/pypi/django-pagination-bootstrap
.. _django-sorting-bootstrap: http://pypi.python.org/pypi/django-sorting-bootstrap
