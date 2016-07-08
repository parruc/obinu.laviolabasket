# -*- coding: utf-8 -*-
import logging
import os
from datetime import datetime

from zope.component import getMultiAdapter, getUtility
from zope.interface import implementer
from zope.intid.interfaces import IIntIds

import transaction
from parruc.violareggiocalabria import _
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from z3c.relationfield import RelationValue

logger = logging.getLogger('parruc.violareggiocalabria')


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'parruc.violareggiocalabria:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    _create_structure()
    _create_content()
    transaction.commit()


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
base_perm = "parruc.violareggiocalabria: Add "
folders = [{"title": _("Giocatori"), "permission": base_perm + "Giocatore", "exclude_from_nav": True},
           {"title": _("Notizie"), "permission": base_perm + "News Item", "exclude_from_nav": False},
           {"title": _("Partite"), "permission": base_perm + "Partita", "exclude_from_nav": True},
           {"title": _("Sponsor"), "permission": base_perm + "Sponsor", "exclude_from_nav": True},
           {"title": _("Squadre"), "permission": base_perm + "Squadra", "exclude_from_nav": True},
           {"title": _("Video"), "permission": base_perm + "Video", "exclude_from_nav": True},
           {"title": _("Slides"), "permission": base_perm + "Slide", "exclude_from_nav": True}, ]


def load_image(path):
    from plone.namedfile import NamedBlobImage
    filename = path.split("/")[-1]
    data = open(path, 'r').read()
    return NamedBlobImage(data=data,
                          contentType='image/png',
                          filename=u''+filename, )


squadre = [{"title": "Viola Reggiocalabria",
            "played": 10, "points": 15},
           {"title": "Chicago Bulls",
            "played": 10, "points": 30},
           {"title": "Predappio Basket",
            "played": 10, "points": 0}]

partite = [{"title": "Vittoria al cardiopalma",
            "home_index": 0, "away_index": 1,
            "score_home": 100, "score_away": 99,
            "start": datetime(2016, 6, 1, 15, 30, 0), },
           {"title": "Grande vittoria fuori casa",
            "home_index": 2, "away_index": 0,
            "score_home": 120, "score_away": 45,
            "start": datetime(2016, 7, 1, 19, 30, 0), },
           {"title": "Sconfitta di misura",
            "home_index": 1, "away_index": 0,
            "score_home": 98, "score_away": 110,
            "start": datetime(2016, 8, 1, 21, 30, 0), }, ]


def _create_structure():
    portal = api.portal.get()
    for folder in folders:
        if api.content.find(portal_type='Folder', Title=folder["title"]):
            continue
        obj = api.content.create(container=portal, type="Folder",
                                 title=folder["title"],
                                 exclude_from_nav=folder["exclude_from_nav"])
        obj.manage_permission(folder["permission"], roles=['Editor'],
                              acquire=True)
        api.content.transition(obj=obj, transition='publish')


def _create_content():
    portal = api.portal.get()
    logo_path = os.path.join(os.path.dirname(__file__), 'browser', 'static',
                             'violareggiocalabria-logo.png')
    if not api.content.find(portal_type='Homepage'):
        hp = api.content.create(container=portal,
                                title="index",
                                type="Homepage")
        portal.setDefaultPage(hp.id)
        api.content.transition(obj=hp, transition='publish')
    folder = portal.get("squadre")
    teams = []
    for squadra in squadre:
        if api.content.find(portal_type='Squadra', Title=squadra["title"]):
            continue
        squadra["logo"] = load_image(unicode(logo_path))
        obj = api.content.create(container=folder, type="Squadra", **squadra)
        obj.logo = load_image(logo_path)
        teams.append(RelationValue(getUtility(IIntIds).getId(obj)))
        api.content.transition(obj=obj, transition='publish')
    folder = portal.get("partite")
    for partita in partite:
        if api.content.find(portal_type='Partita', Title=partita["title"]):
            continue
        partita['home'] = teams[partita["home_index"]]
        partita['away'] = teams[partita["away_index"]]
        obj = api.content.create(container=folder, type="Partita", **partita)
        api.content.transition(obj=obj, transition='publish')
