# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from version import get_git_version

def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''

# Use the docstring of the __init__ file to be the description
DESC = " ".join(__import__('crud_utils').__doc__.splitlines()).strip()

setup(
    name = "django-crud-utils",
    version = get_git_version(),
    url = 'https://github.com/staticdev/django-crud-utils',
    author = 'Thiago Carvalho',
    author_email = 'thiagocavila@gmail.com',
    description = DESC,
    long_description = read_file('README'),
    packages = find_packages(),
    include_package_data = True,
    install_requires=[
        'Django >= 1.2.0',
        'django-pagination-bootstrap',
        'django-sorting-bootstrap',
        'django-floppyforms',
    ],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
    ],
)
