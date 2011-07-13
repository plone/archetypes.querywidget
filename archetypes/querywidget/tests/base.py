import unittest2 as unittest

from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing.layers import IntegrationTesting
from plone.testing import z2
from zope.configuration import xmlconfig


class ArchetypesQueryWidgetLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import archetypes.querywidget
        xmlconfig.file('configure.zcml', archetypes.querywidget,
                       context=configurationContext)

        import plone.app.collection
        xmlconfig.file('configure.zcml', plone.app.collection,
                       context=configurationContext)
        z2.installProduct(app, 'plone.app.collection')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.app.collection:default')
        portal.acl_users.userFolderAddUser('admin',
                                           'secret',
                                           ['Manager'],
                                           [])
        login(portal, 'admin')

        # enable workflow for browser tests
        workflow = portal.portal_workflow
        workflow.setDefaultChain('simple_publication_workflow')

        # add a page, so we can test with it
        portal.invokeFactory("Document",
                             "document",
                             title="Document Test Page")
        # and add a collection so we can test the widget
        portal.invokeFactory("Collection",
                             "collection",
                             title="Test Collection")

        workflow.doActionFor(portal.document, "publish")
        workflow.doActionFor(portal.collection, "publish")


QUERYWIDGET_FIXTURE = ArchetypesQueryWidgetLayer()

QUERYWIDGET_INTEGRATION_TESTING =\
                IntegrationTesting(bases=(QUERYWIDGET_FIXTURE,),
                name="ArchetypesQueryWidget:Integration")


class ArchetypesQueryWidgetTestCase(unittest.TestCase):
    layer = QUERYWIDGET_INTEGRATION_TESTING
