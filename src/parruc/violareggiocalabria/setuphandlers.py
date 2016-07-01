# -*- coding: utf-8 -*-
import os
from datetime import datetime

from zope.component import getUtility
from zope.interface import implementer
from zope.intid.interfaces import IIntIds

from parruc.violareggiocalabria import _
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from z3c.relationfield import RelationValue


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
    _create_content()


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.

folders = [_("Squadre"), _("Video"),
           _("Partite"), _("Notizie"),
           _("Giocatori"), _("Sponsor")]


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
            "home_index":0, "away_index": 1,
            "score_home": 100, "score_away": 99,
            "start": datetime(2016, 6, 1, 15, 30, 0),},
            {"title": "Grande vittoria fuori casa",
            "home_index":2, "away_index": 0,
             "score_home": 120, "score_away": 45,
             "start": datetime(2016, 7, 1, 19, 30, 0),},
             {"title": "Sconfitta di misura",
              "home_index":1, "away_index": 0,
              "score_home": 98, "score_away": 110,
              "start": datetime(2016, 8, 1, 21, 30, 0),},]


def _create_content():
    portal = api.portal.get()
    logo_path = os.path.join(os.path.dirname(__file__), 'browser', 'static',
                             'violareggiocalabria-logo.png')
    for folder in folders:
        obj = api.content.create(container=portal, type="Folder", title=folder)
        api.content.transition(obj=obj, transition='publish')
    folder = portal.get("squadre")
    teams = []
    for squadra in squadre:
        squadra["logo"] = load_image(unicode(logo_path))
        obj = api.content.create(container=folder, type="Squadra", **squadra)
        obj.logo = load_image(logo_path)
        teams.append(RelationValue(getUtility(IIntIds).getId(obj)))
        api.content.transition(obj=obj, transition='publish')
    folder = portal.get("partite")
    for partita in partite:
        partita['home'] = teams[partita["home_index"]]
        partita['away'] = teams[partita["away_index"]]
        import ipdb; ipdb.set_trace()
        obj = api.content.create(container=folder, type="Partita", **partita)
        api.content.transition(obj=obj, transition='publish')
