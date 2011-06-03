"""
    QueryField field class
"""

from __future__ import nested_scopes

from AccessControl import ClassSecurityInfo
from Products.Archetypes.Field import ObjectField
from Products.Archetypes.Field import registerField
from archetypes.querywidget.interfaces import IQueryField
from zope.interface import implements
from zope.app.component.hooks import getSite

from plone.app.querystring.querybuilder import QueryBuilder


class QueryField(ObjectField):
    """QueryField for storing query"""
    implements(IQueryField)
    _properties = ObjectField._properties.copy()

    security = ClassSecurityInfo()

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    def get(self, instance, **kwargs):
        """Get the query dict from the request or from the object"""
        raw = kwargs.get('raw', None)
        value = self.getRaw(instance)
        if raw == True:
            # We actually wanted the raw value, should have called getRaw
            return value
        querybuilder = QueryBuilder(instance, getSite().REQUEST)

        sort_order = 'reverse' if instance.getSort_reversed() else 'ascending'
        return querybuilder(query=value, sort_on=instance.getSort_on(), sort_order=sort_order)

    def getRaw(self, instance, **kwargs):
        return ObjectField.get(self, instance, **kwargs) or ()


registerField(QueryField,
              title='QueryField',
              description=('query field for storing a query'))
