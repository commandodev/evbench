from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='bench',
      version=version,
      description="Bench mark tool built on eventlet",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ben Ford',
      author_email='ben@bothead.co.uk',
      url='http://github.com/boothead/bench',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
