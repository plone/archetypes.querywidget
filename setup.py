from setuptools import setup, find_packages

version = '1.0.6'

tests_require = ['plone.app.testing']

setup(name='archetypes.querywidget',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      classifiers=[
        "Framework :: Plone",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/archetypes.querywidget',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['archetypes'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.querystring>=1.0.3dev',
          'plone.app.jquerytools',
      ],
      tests_require = tests_require,
      extras_require = {
          'tests': tests_require,
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
