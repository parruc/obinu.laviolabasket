# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from obinu.laviolabasket.testing import OBINU_LAVIOLABASKET_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that obinu.laviolabasket is properly installed."""

    layer = OBINU_LAVIOLABASKET_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if obinu.laviolabasket is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'obinu.laviolabasket'))

    def test_browserlayer(self):
        """Test that IObinuLaviolabasketLayer is registered."""
        from obinu.laviolabasket.interfaces import (
            IObinuLaviolabasketLayer)
        from plone.browserlayer import utils
        self.assertIn(IObinuLaviolabasketLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = OBINU_LAVIOLABASKET_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['obinu.laviolabasket'])

    def test_product_uninstalled(self):
        """Test if obinu.laviolabasket is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'obinu.laviolabasket'))

    def test_browserlayer_removed(self):
        """Test that IObinuLaviolabasketLayer is removed."""
        from obinu.laviolabasket.interfaces import IObinuLaviolabasketLayer
        from plone.browserlayer import utils
        self.assertNotIn(IObinuLaviolabasketLayer, utils.registered_layers())
