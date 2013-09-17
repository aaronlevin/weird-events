from setuptools import setup, find_packages
import sys, os

version = '1.0'

install_requires = [
    # -*- Extra requirements: -*-
    ]

setup(name='weird_events',
      version=version,
      description="Your guide to the Canadian underground (wrapped in JSON and delivered to your intraweb).",
      long_description="",
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          ],
      keywords='',
      author='Weird Canada',
      author_email='',
      url='http://weirdcanada.ca/',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      """,
      )
