from copy import deepcopy
from AccessControl import ClassSecurityInfo
from Acquisition import aq_inner, aq_parent
from archetypes.querywidget.interfaces import IQueryField
from Products.Archetypes.Field import ObjectField
from Products.Archetypes.Field import registerField
from zope.interface import implements
from zope.site.hooks import getSite
from plone.app.querystring.querybuilder import QueryBuilder


class QueryField(ObjectField):
    """QueryField for storing query"""

    implements(IQueryField)
    _properties = ObjectField._properties.copy()

    security = ClassSecurityInfo()

    def get(self, instance, **kwargs):
        """Get the query dict from the request or from the object"""
        raw = kwargs.get('raw', None)
        # By default we want to merge our query with our parent query.
        recursive = kwargs.get('recursive', True)
        value = self.getRaw(instance, recursive=recursive)
        if raw:
            # We actually wanted the raw value, should have called getRaw
            return value
        querybuilder = QueryBuilder(instance, getSite().REQUEST)

        sort_on = kwargs.get('sort_on', instance.getSort_on())
        sort_order = 'reverse' if instance.getSort_reversed() else 'ascending'
        limit = kwargs.get('limit', instance.getLimit())
        return querybuilder(query=value, batch=kwargs.get('batch', False),
            b_start=kwargs.get('b_start', 0), b_size=kwargs.get('b_size', 30),
            sort_on=sort_on, sort_order=sort_order,
            limit=limit, brains=kwargs.get('brains', False))

    def getRaw(self, instance, **kwargs):
        recursive = kwargs.get('recursive', False)
        value = deepcopy(ObjectField.get(self, instance, **kwargs) or [])
        if recursive:
            parent = aq_parent(aq_inner(instance))
            if self.getRaw(parent):
                # The parent has the same field.  Combine it recursively.
                parent_value = self.getRaw(parent, recursive=recursive)
                for parent_row in parent_value:
                    parent_index = parent_row['i']
                    found = False
                    for own_row in value:
                        own_index = own_row['i']
                        if own_index == parent_index:
                            found = True
                            break
                    if not found:
                        # parent index is not in own index, so we add it
                        value.append(parent_row)

        return value


registerField(QueryField, title='QueryField',
    description=('query field for storing a query'))
