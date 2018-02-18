#!/usr/bin/env python

from distutils.core import setup

setup(
  name = 'hake',
  version = '0.1.0',
  description = 'A simple task manager inspired by Rake',
  author = 'Nickolay Ilyushin',
  author_email = 'nickolay02@inbox.ru',
  url = 'https://github.com/handicraftsman/hake',
  packages = ['hake'],
  classifiers = [
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Lisp',
    'Programming Language :: Hy',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Utilities'
  ]
)
