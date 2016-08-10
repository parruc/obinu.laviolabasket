# -*- coding: utf-8 -*-
from initial_data import folders
from initial_data import leagues
from initial_data import news
from initial_data import pages
from initial_data import partite
from initial_data import partners
from initial_data import players
from initial_data import slides
from initial_data import sponsors
from initial_data import teams
from initial_data import videos
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from z3c.relationfield import RelationValue
from zc.relation.interfaces import ICatalog
from zope.component import createObject
from zope.component import getUtility
from zope.interface import implementer
from zope.intid.interfaces import IIntIds

import logging
import os
import transaction


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


def obj_to_rel(obj):
    return RelationValue(getUtility(IIntIds).getId(obj))


def publish_and_reindex(obj):
    obj.reindexObject()
    references_catalog = getUtility(ICatalog)
    references_catalog.index(obj)
    if api.content.get_state(obj=obj) != "published":
        api.content.transition(obj=obj, transition='publish')


def get_object_by_title(obj_list, title):
    for obj in obj_list:
        if obj.to_object.title == title:
            return obj


def load_image(path, mime):
    from plone.namedfile import NamedBlobImage
    filename = path.split("/")[-1]
    data = open(path, 'r').read()
    return NamedBlobImage(data=data,
                          contentType=mime,
                          filename=u''+filename, )


def _add_subobjs(obj, field_name, subobj_type, data_list):
    subobjs = []
    for count, data in enumerate(data_list):
        subobj = createObject(subobj_type, **data)
        subobjs.append(subobj)
    setattr(obj, field_name, subobjs)


def _create_structure():
    portal = api.portal.get()
    permission = view = None
    for folder in folders:
        if "permission" in folder:
            permission = folder.pop("permission")
        if "view" in folder:
            view = folder.pop("view")
        if api.content.find(portal_type='Folder', Title=folder["title"]):
            continue
        obj = api.content.create(container=portal, type="Folder", **folder)
        if permission:
            obj.manage_permission(permission, roles=['Editor'],
                                  acquire=True)
        if view:
            obj.setLayout(view)
        publish_and_reindex(obj)


def _create_content():
    portal = api.portal.get()
    teams_rels = slides_rels = pages_rels = leagues_rels = []
    page_brains = api.content.find(portal_type='Document')
    if page_brains:
        pages_rels = [p.getObject() for p in page_brains]
    else:
        for page in pages:
            parent = portal.get(page.get('parent'), None)
            if not parent:
                parent = portal
            obj = api.content.create(container=parent, type="Document", **page)
            pages_rels.append(obj)
            publish_and_reindex(obj)
    league_brains = api.content.find(portal_type='League')
    pages_rels = map(obj_to_rel, pages_rels)
    if league_brains:
        leagues_rels = [l.getObject() for l in league_brains]
    else:
        folder = portal.get("leagues")
        for league in leagues:
            obj = api.content.create(container=folder, type="League",
                                     **league)
            publish_and_reindex(obj)
            leagues_rels.append(obj)
    leagues_rels = map(obj_to_rel, leagues_rels)
    team_brains = api.content.find(portal_type='Squadra')
    if team_brains:
        teams_rels = [t.getObject() for t in team_brains]
    else:
        folder = portal.get("squadre")
        for team in teams:
            logo_path = os.path.join(base_img_path, team["image_logo"])
            teaser_path = os.path.join(base_img_path, team["image_teaser"])
            if "league" in team and team["league"]:
                league = team.pop("league")
                team["league"] = get_object_by_title(leagues_rels, league)
            obj = api.content.create(container=folder, type="Squadra",
                                     **team)
            obj.image_logo = load_image(logo_path, 'image/png')
            obj.image_teaser = load_image(teaser_path, 'image/jpg')
            teams_rels.append(obj)
            publish_and_reindex(obj)
    teams_rels = map(obj_to_rel, teams_rels)
    if not api.content.find(portal_type='Partita'):
        folder = portal.get("partite")
        for partita in partite:
            partita['home'] = teams_rels[partita["home_index"]]
            partita['away'] = teams_rels[partita["away_index"]]
            obj = api.content.create(container=folder, type="Partita",
                                     **partita)
            publish_and_reindex(obj)
    slide_brains = api.content.find(portal_type='Slide')
    if slide_brains:
        slides_rels = [s.getObject() for s in slide_brains]
    else:
        folder = portal.get("slide")
        for count, slide in enumerate(slides):
            slide["link"] = pages_rels[count+1]
            obj = api.content.create(container=folder, type="Slide", **slide)
            image_path = os.path.join(base_img_path, slide["image"])
            obj.image = load_image(image_path, 'image/jpg')
            slides_rels.append(obj)
            publish_and_reindex(obj)
    slides_rels = map(obj_to_rel, slides_rels)
    if not api.content.find(portal_type='Video'):
        folder = portal.get("video")
        for video in videos:
            obj = api.content.create(container=folder, type="Video", **video)
            publish_and_reindex(obj)
    if not api.content.find(portal_type='Giocatore'):
        for player in players:
            viola_brain = api.content.find(portal_type='Squadra',
                                           is_viola=True)
            if len(viola_brain) > 0:
                obj = viola_brain[0].getObject()
                player["team"] = RelationValue(getUtility(IIntIds).getId(obj))
            folder = portal.get("roster")
            player["title"] = player["surname"] + " " + player["name"]
            stats = None
            if "stats" in player:
                stats = player.pop("stats")
            obj = api.content.create(container=folder, type="Giocatore",
                                     **player)
            if stats:
                _add_subobjs(obj, "stats", "StatisticheGiocatore", stats)
            image_path = os.path.join(base_img_path, 'player.jpg')
            obj.image = load_image(image_path, 'image/jpg')
            image_bg_path = os.path.join(base_img_path, 'players-bg.jpg')
            obj.image_back = load_image(image_bg_path, 'image/jpg')
            publish_and_reindex(obj)
    if not api.content.find(portal_type='News Item'):
        folder = portal.get("news")
        for new in news:
            obj = api.content.create(container=folder, type="News Item", **new)
            publish_and_reindex(obj)
    if not api.content.find(portal_type='Partner'):
        folder = portal.get("partner")
        for partner in partners:
            image_path = os.path.join(base_img_path, partner["image"])
            obj = api.content.create(container=folder, type="Partner",
                                     **partner)
            obj.image = load_image(image_path, 'image/png')
            publish_and_reindex(obj)
    if not api.content.find(portal_type='Sponsor'):
        folder = portal.get("sponsor")
        for sponsor in sponsors:
            image_path = os.path.join(base_img_path, sponsor["image"])
            obj = api.content.create(container=folder, type="Sponsor",
                                     **sponsor)
            obj.image = load_image(image_path, 'image/png')
            publish_and_reindex(obj)
    if not api.content.find(portal_type='Homepage'):
        league = get_object_by_title(leagues_rels, "A2")
        hp = api.content.create(container=portal, title="index.html",
                                type="Homepage", slides=slides_rels,
                                exclude_from_nav=True, league_hp=league)
        portal.setDefaultPage(hp.id)
        publish_and_reindex(obj)
