# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

from parruc.violareggiocalabria.testing import \
    PARRUC_VIOLAREGGIOCALABRIA_INTEGRATION_TESTING  # noqa
from plone import api


class TestSetup(unittest.TestCase):
    """Test that parruc.violareggiocalabria is properly installed."""

    layer = PARRUC_VIOLAREGGIOCALABRIA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if parruc.violareggiocalabria is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'parruc.violareggiocalabria'))

    def test_browserlayer(self):
        """Test that IParrucViolareggiocalabriaLayer is registered."""
        from parruc.violareggiocalabria.interfaces import (
            IParrucViolareggiocalabriaLayer)
        from plone.browserlayer import utils
        self.assertIn(IParrucViolareggiocalabriaLayer,
                      utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PARRUC_VIOLAREGGIOCALABRIA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['parruc.violareggiocalabria'])

    def test_product_uninstalled(self):
        """Test if parruc.violareggiocalabria is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'parruc.violareggiocalabria'))

    def test_browserlayer_removed(self):
        """Test that IParrucViolareggiocalabriaLayer is removed."""
        from parruc.violareggiocalabria.interfaces import \
            IParrucViolareggiocalabriaLayer
        from plone.browserlayer import utils
        self.assertNotIn(IParrucViolareggiocalabriaLayer,
                         utils.registered_layers())
