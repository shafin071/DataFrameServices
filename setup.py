import os
from os import path
from setuptools import setup



setup_directory = path.abspath(path.dirname(__file__))
with open(path.join(setup_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='dfs',
      version='1.1.3',
      author="Shafin M",
      author_email="shafinmohammed071@gmail.com",
      description='DataFrame Services built on top of Pandas and Numpy',
      packages=['dfs'],
      zip_safe=False,
      install_requires = [ f'pandas' ],
      setup_requires = [ f'pandas' ],
      long_description = long_description,
      long_description_content_type='text/markdown'
      )


