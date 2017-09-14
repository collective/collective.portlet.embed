from setuptools import setup, find_packages
import os

version = '1.3.0'

setup(name='collective.portlet.embed',
      version=version,
      description="Embed an HTML snippet in a Plone portlet",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        ],
      keywords='plone portlet embed iframe',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='toutpt@gmail.com',
      maintainer='keul',
      maintainer_email='luca@keul.it',
      url='https://github.com/collective/collective.portlet.embed',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.portlet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone>=4.0',
          'z3c.form',
      ],
      extras_require=dict(
          test=['plone.app.testing', 'plone.app.robotframework', 'selenium'],
      ),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
