# -*- coding: utf-8 -*-
import logging
import os

from zope.component import getUtility
from zope.interface import implementer
from zope.intid.interfaces import IIntIds

import transaction
from initial_data import (folders, news, pages, partite, partners, players,
                          slides, sponsors, teams, videos)
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


base_img_path = os.path.join(os.path.dirname(__file__), 'browser', 'static')


def load_image(path, mime):
    from plone.namedfile import NamedBlobImage
    filename = path.split("/")[-1]
    data = open(path, 'r').read()
    return NamedBlobImage(data=data,
                          contentType=mime,
                          filename=u''+filename, )


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
    folder = portal.get("squadre")
    teams_rels = slides_rels = pages_rels = []
    if not api.content.find(portal_type='Document'):
        for page in pages:
            obj = api.content.create(container=portal, type="Document", **page)
            pages_rels.append(RelationValue(getUtility(IIntIds).getId(obj)))
            api.content.transition(obj=obj, transition='publish')
    if not api.content.find(portal_type='Squadra'):
        for team in teams:
            logo_path = os.path.join(base_img_path, team["image_logo"])
            teaser_path = os.path.join(base_img_path, team["image_teaser"])
            obj = api.content.create(container=folder, type="Squadra",
                                     **team)
            obj.image_logo = load_image(logo_path, 'image/png')
            obj.image_teaser = load_image(teaser_path, 'image/jpg')
            teams_rels.append(RelationValue(getUtility(IIntIds).getId(obj)))
            api.content.transition(obj=obj, transition='publish')
    folder = portal.get("partite")
    if not api.content.find(portal_type='Partita'):
        for partita in partite:
            partita['home'] = teams_rels[partita["home_index"]]
            partita['away'] = teams_rels[partita["away_index"]]
            obj = api.content.create(container=folder, type="Partita",
                                     **partita)
            api.content.transition(obj=obj, transition='publish')
    folder = portal.get("slides")
    if not api.content.find(portal_type='Slide'):
        for count, slide in enumerate(slides):
            slide["link"] = pages_rels[count+1]
            obj = api.content.create(container=folder, type="Slide", **slide)
            image_path = os.path.join(base_img_path, slide["image"])
            obj.image = load_image(image_path, 'image/jpg')
            slides_rels.append(RelationValue(getUtility(IIntIds).getId(obj)))
            api.content.transition(obj=obj, transition='publish')
    folder = portal.get("video")
    if not api.content.find(portal_type='Video'):
        for video in videos:
            obj = api.content.create(container=folder, type="Video", **video)
            api.content.transition(obj=obj, transition='publish')
    folder = portal.get("roster")
    if not api.content.find(portal_type='Giocatore'):
        for player in players:
            player["title"] = player["surname"] + " " + player["name"]
            image_path = os.path.join(base_img_path, 'player.jpg')
            obj = api.content.create(container=folder, type="Giocatore",
                                     **player)
            obj.image = load_image(image_path, 'image/jpg')
            api.content.transition(obj=obj, transition='publish')
    folder = portal.get("news")
    if not api.content.find(portal_type='News Item'):
        for new in news:
            obj = api.content.create(container=folder, type="News Item", **new)
            api.content.transition(obj=obj, transition='publish')
    folder = portal.get("partner")
    if not api.content.find(portal_type='Partner'):
        for partner in partners:
            image_path = os.path.join(base_img_path, partner["image"])
            obj = api.content.create(container=folder, type="Partner",
                                     **partner)
            obj.image = load_image(image_path, 'image/png')
            api.content.transition(obj=obj, transition='publish')
    folder = portal.get("sponsor")
    if not api.content.find(portal_type='Sponsor'):
        for sponsor in sponsors:
            image_path = os.path.join(base_img_path, sponsor["image"])
            obj = api.content.create(container=folder, type="Sponsor",
                                     **sponsor)
            obj.image = load_image(image_path, 'image/png')
            api.content.transition(obj=obj, transition='publish')
    if not api.content.find(portal_type='Homepage'):
        hp = api.content.create(container=portal, title="index",
                                type="Homepage", slides=slides_rels,
                                exclude_from_nav=True, )
        portal.setDefaultPage(hp.id)
        api.content.transition(obj=hp, transition='publish')
