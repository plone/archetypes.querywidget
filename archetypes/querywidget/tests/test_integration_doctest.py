import unittest
import doctest

from Testing import ZopeTestCase as ztc

import base


def test_suite():
    # Wire in integration.txt tests as doctests in the integration layer
    return unittest.TestSuite([
        ztc.ZopeDocFileSuite(
            'tests/integration.txt', package='archetypes.querywidget',
            test_class=base.ArchetypesQueryWidgetTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                        doctest.NORMALIZE_WHITESPACE |
                        doctest.ELLIPSIS),
        ])
