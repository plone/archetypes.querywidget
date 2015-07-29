archetypes.querywidget
======================

Overall Integration
-------------------

This package contains the archetypes field and widget used in
plone.app.collection to select the search criteria of the collection.

First login as portal owner::

    >>> app = self.layer['app']
    >>> from plone.testing.z2 import Browser
    >>> browser = Browser(app)
    >>> browser.handleErrors = False
    >>> browser.addHeader('Authorization', 'Basic admin:secret')

We added a collection in the test layer, so we check if the query field
is there, and see if it's rendered::

    >>> portal = self.layer['portal']
    >>> field = portal.collection.getField('query')
    >>> from archetypes.querywidget.field import QueryField
    >>> isinstance(field, QueryField)
    True
    >>> browser.open(portal.collection.absolute_url()+'/edit')
    >>> 'id="archetypes-fieldname-query"' in browser.contents
    True
    >>> 'class="field ArchetypesQueryWidget' in browser.contents
    True

Bug Checks
----------

Check for bug `#13144 <https://dev.plone.org/ticket/13144>`_::

    >>> field = portal.collection.getField('query')
    >>> field.set(portal.collection, [{'i': 'start', 'o': 'some.namespace.op.foo'}])
    >>> raw1 = field.get(portal.collection, raw=True)
    >>> raw1
    [{'i': 'start', 'o': 'some.namespace.op.foo'}]

    >>> length1 = len(raw1)
    >>> raw1.append({'i': 'end', 'o': 'some.namespace.op.bar'})
    >>> raw2 = field.get(portal.collection, raw=True)

Now the amount of entries in raw2 has to be the same as in raw1::

    >>> length1 == len(raw2)
    True

Nested
------

Test a nested Collection.  TODO: This is not allowed by default and
needs an unreleased plone.app.collection.  Maybe test this in a
different way.

getRaw and get(raw=True) should always return the same value.  With
recursive=True, the value of the parent is shown::

    >>> nested = portal.collection.collection2
    >>> field = nested.getField('query')
    >>> field.getRaw(nested)
    []
    >>> field.get(nested, raw=True)
    []
    >>> field.getRaw(nested, recursive=True)
    [{'i': 'start', 'o': 'some.namespace.op.foo'}]
    >>> field.get(nested, raw=True, recursive=True)
    [{'i': 'start', 'o': 'some.namespace.op.foo'}]

Set a value and try again::

    >>> field.set(nested, [{'i': 'middle', 'o': 'some.namespace.op.quux'}])
    >>> field.getRaw(nested)
    [{'i': 'middle', 'o': 'some.namespace.op.quux'}]
    >>> field.get(nested, raw=True)
    [{'i': 'middle', 'o': 'some.namespace.op.quux'}]
    >>> field.getRaw(nested, recursive=True)
    [{'i': 'middle', 'o': 'some.namespace.op.quux'},
     {'i': 'start', 'o': 'some.namespace.op.foo'}]
    >>> field.get(nested, raw=True, recursive=True)
    [{'i': 'middle', 'o': 'some.namespace.op.quux'},
     {'i': 'start', 'o': 'some.namespace.op.foo'}]

Our parent can only add to our query items, not override them::

    >>> field.set(nested, [{'i': 'start', 'o': 'some.namespace.op.quux'}])
    >>> field.getRaw(nested)
    [{'i': 'start', 'o': 'some.namespace.op.quux'}]
    >>> field.get(nested, raw=True)
    [{'i': 'start', 'o': 'some.namespace.op.quux'}]
    >>> field.getRaw(nested, recursive=True)
    [{'i': 'start', 'o': 'some.namespace.op.quux'}]
    >>> field.get(nested, raw=True, recursive=True)
    [{'i': 'start', 'o': 'some.namespace.op.quux'}]
