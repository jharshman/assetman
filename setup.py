#!/usr/bin/python

from distutils.core import setup

setup(name='assetman',
      version='0.2.0', # also update in __init__.py
      description='AssetMan asset manager',
      url="http://github.com/bitly/assetman",
      license="Apache Software License",
      author='Will McCutchen',
      author_email="wm@bit.ly",
      maintainer="Jehiah Czebotar",
      maintainer_email="jehiah@gmail.com",
      packages=['assetman', 'assetman/parsers', 'assetman/tornadoutils', 'assetman/django_assetman', 
                        'assetman/django_assetman/templatetags'],
      install_requires=['simplejson',
                        'multiprocessing',
                       ],
      classifiers = [
                     "Programming Language :: Python :: 2",
                     "Programming Language :: Python :: 2.7",
                     ],
      scripts=['scripts/assetman_compile']
)
