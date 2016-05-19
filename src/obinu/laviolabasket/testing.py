# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import obinu.laviolabasket


class ObinuLaviolabasketLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=obinu.laviolabasket)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'obinu.laviolabasket:default')


OBINU_LAVIOLABASKET_FIXTURE = ObinuLaviolabasketLayer()


OBINU_LAVIOLABASKET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(OBINU_LAVIOLABASKET_FIXTURE,),
    name='ObinuLaviolabasketLayer:IntegrationTesting'
)


OBINU_LAVIOLABASKET_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(OBINU_LAVIOLABASKET_FIXTURE,),
    name='ObinuLaviolabasketLayer:FunctionalTesting'
)


OBINU_LAVIOLABASKET_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        OBINU_LAVIOLABASKET_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ObinuLaviolabasketLayer:AcceptanceTesting'
)
