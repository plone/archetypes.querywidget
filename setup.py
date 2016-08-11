from setuptools import setup, find_packages

version = '1.1.3'

tests_require = ['plone.app.testing']

setup(
    name='archetypes.querywidget',
    version=version,
    description=("Archetypes.querywidget implements a widget "
                 "for creating catalog queries using an "
                 "email-filtering-like interface, as found "
                 "in GMail or Apple Mail."),
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='archetypes query widget collection topic',
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
        'plone.app.querystring>=1.2.2',  # custom_query support
        'plone.app.jquery>=1.7.2',
        'plone.app.jquerytools',
    ],
    tests_require=tests_require,
    extras_require={
        'tests': tests_require,
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target=plone
    """,
)
