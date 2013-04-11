from copy import deepcopy
from AccessControl import ClassSecurityInfo
from Acquisition import aq_inner, aq_parent
from archetypes.querywidget.interfaces import IQueryField
from Products.Archetypes.Field import ObjectField
from Products.Archetypes.Field import registerField
from zope.component import getMultiAdapter
from zope.interface import implements
from zope.site.hooks import getSite


class QueryField(ObjectField):
    """QueryField for storing query"""

    implements(IQueryField)
    _properties = ObjectField._properties.copy()

    security = ClassSecurityInfo()

    def get(self, instance, **kwargs):
        """Get the query dict from the request or from the object"""
        raw = kwargs.get('raw', None)
        if raw:
            # We actually wanted the raw value, should have called getRaw
            value = self.getRaw(instance, **kwargs)
            return value
        parent = kwargs.get('parent', None)
        if parent:
            # We want the parent value, if it is a good parent
            del kwargs['parent']
            parent = aq_parent(aq_inner(instance))
            value = self.get(parent, **kwargs)
            return value
        # By default we want to merge our query with our parent query.
        recursive = kwargs.get('recursive', True)
        value = self.getRaw(instance, recursive=recursive)
        querybuilder = getMultiAdapter((instance, getSite().REQUEST),
                                       name='querybuilderresults')

        sort_on = kwargs.get('sort_on', instance.getSort_on())
        sort_order = 'reverse' if instance.getSort_reversed() else 'ascending'
        limit = kwargs.get('limit', instance.getLimit())
        return querybuilder(query=value, batch=kwargs.get('batch', False),
            b_start=kwargs.get('b_start', 0), b_size=kwargs.get('b_size', 30),
            sort_on=sort_on, sort_order=sort_order,
            limit=limit, brains=kwargs.get('brains', False))

    def getRaw(self, instance, **kwargs):
        parent = kwargs.get('parent', None)
        if parent:
            # We want the parent value, if it is a good parent
            del kwargs['parent']
            parent = aq_parent(aq_inner(instance))
            value = self.getRaw(parent, **kwargs)
            return value
        recursive = kwargs.get('recursive', False)
        value = deepcopy(ObjectField.get(self, instance, **kwargs) or [])
        if recursive:
            parent = aq_parent(aq_inner(instance))
            if self.getRaw(parent):
                # The parent has the same field.  Combine it recursively.
                # TODO: it might just be a different field with the same name...
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
