# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from obinu.laviolabasket.testing import OBINU_LAVIOLABASKET_INTEGRATION_TESTING  # noqa
from obinu.laviolabasket.interfaces import ISponsor

import unittest2 as unittest


class SponsorIntegrationTest(unittest.TestCase):

    layer = OBINU_LAVIOLABASKET_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Sponsor')
        schema = fti.lookupSchema()
        self.assertEqual(ISponsor, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Sponsor')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Sponsor')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ISponsor.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Sponsor', 'Sponsor')
        self.assertTrue(
            ISponsor.providedBy(self.portal['Sponsor'])
        )
