# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import parruc.violareggiocalabria


class ParrucViolareggiocalabriaLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=parruc.violareggiocalabria)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'parruc.violareggiocalabria:default')


PARRUC_VIOLAREGGIOCALABRIA_FIXTURE = ParrucViolareggiocalabriaLayer()


PARRUC_VIOLAREGGIOCALABRIA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PARRUC_VIOLAREGGIOCALABRIA_FIXTURE,),
    name='ParrucViolareggiocalabriaLayer:IntegrationTesting'
)


PARRUC_VIOLAREGGIOCALABRIA_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PARRUC_VIOLAREGGIOCALABRIA_FIXTURE,),
    name='ParrucViolareggiocalabriaLayer:FunctionalTesting'
)


PARRUC_VIOLAREGGIOCALABRIA_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PARRUC_VIOLAREGGIOCALABRIA_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ParrucViolareggiocalabriaLayer:AcceptanceTesting'
)
