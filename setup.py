#!/usr/bin/env python

from distutils.core import setup

setup(name='django-id-obfuscator',
      version='1.0',
      description='Non-secure hashing/obfuscation of integers (ideal for use in URLs to discourage snooping)',
      author='Jordan Reiter',
      author_email='jordanreiter@gmail.com',
      url='https://github.com/JordanReiter/django-id-obfuscator',
      packages=['id_obfuscator'],
     )
