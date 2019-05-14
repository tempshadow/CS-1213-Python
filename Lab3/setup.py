#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages

setup(name='lab3',
      version='1.0',
      description='CS1213 Lab3',
      author=[
          "Austin Graham"
      ],
      author_email=[
          "austin.p.graham-1@ou.edu"
      ],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      entry_points = {
          'console_scripts': [
              'run_lab3=lab3.scripts.run:main'
          ]
      },
      install_requires=[
      ]
)
