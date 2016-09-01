# -*- coding: utf-8 -*-
from initial_data import banners
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
from zope.component import createObject
from zope.component import getUtility
from zope.event import notify
from zope.interface import implementer
from zope.intid.interfaces import IIntIds
from zope.lifecycleevent import ObjectModifiedEvent

import logging
import os
import transaction


# from zope.lifecycleevent import ObjectModifiedEvent


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
    if api.content.get_state(obj=obj) != "published":
        api.content.transition(obj=obj, transition='publish')
    notify(ObjectModifiedEvent(obj))


def get_rel_by_title(obj_list, title):
    for obj in obj_list:
        if obj.title == title:
            return obj_to_rel(obj)


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
        content_type = "Folder"
        if "slider" in folder:
            content_type = "FolderWithSlider"
        if "permission" in folder:
            permission = folder.pop("permission")
        if "view" in folder:
            view = folder.pop("view")
        if api.content.find(portal_type='Folder', Title=folder["title"]):
            continue
        obj = api.content.create(container=portal, type=content_type, **folder)
        if permission:
            obj.manage_permission(permission, roles=['Editor'],
                                  acquire=True)
        if view:
            obj.setLayout(view)
        publish_and_reindex(obj)


def _create_content():
    portal = api.portal.get()
    teams_objs = []
    slides_objs = []
    pages_objs = []
    leagues_objs = []
    page_brains = api.content.find(portal_type='Document')
    if page_brains:
        pages_objs = [p.getObject() for p in page_brains]
    else:
        for page in pages:
            parent = portal.get(page.get('parent'), None)
            if not parent:
                parent = portal
            obj = api.content.create(container=parent, type="Document", **page)
            pages_objs.append(obj)
            publish_and_reindex(obj)
    league_brains = api.content.find(portal_type='League')
    if league_brains:
        leagues_objs = [l.getObject() for l in league_brains]
    else:
        folder = portal.get("leagues")
        for league in leagues:
            obj = api.content.create(container=folder, type="League",
                                     **league)
            publish_and_reindex(obj)
            leagues_objs.append(obj)
    team_brains = api.content.find(portal_type='Squadra')
    if team_brains:
        teams_objs = [t.getObject() for t in team_brains]
    else:
        folder = portal.get("squadre")
        for team in teams:
            logo_path = os.path.join(base_img_path, team.pop("image_logo"))
            teaser_path = os.path.join(base_img_path, team.pop("image_teaser"))
            obj = api.content.create(container=folder, type="Squadra",
                                     **team)
            obj.league = get_rel_by_title(leagues_objs, team["league_name"])
            obj.image_logo = load_image(logo_path, 'image/png')
            obj.image_teaser = load_image(teaser_path, 'image/jpg')
            teams_objs.append(obj)
            publish_and_reindex(obj)
    slide_brains = api.content.find(portal_type='Slide')
    if slide_brains:
        slides_objs = [s.getObject() for s in slide_brains]
    else:
        folder = portal.get("slide")
        for count, slide in enumerate(slides):
            slide["link"] = obj_to_rel(pages_objs[count+1])
            obj = api.content.create(container=folder, type="Slide", **slide)
            image_path = os.path.join(base_img_path, slide.pop("image"))
            obj.image = load_image(image_path, 'image/jpg')
            slides_objs.append(obj)
            publish_and_reindex(obj)
    if not api.content.find(portal_type='Partita'):
        folder = portal.get("partite")
        folder.slides = [obj_to_rel(s) for s in slides_objs]
        publish_and_reindex(folder)
        for partita in partite:
            partita["competition"] = get_rel_by_title(leagues_objs, "A2")
            obj = api.content.create(container=folder, type="Partita",
                                     **partita)
            image_path = os.path.join(base_img_path, partita.pop("image"))
            obj.image = load_image(image_path, 'image/jpg')
            obj.home = obj_to_rel(teams_objs[partita["home_index"]])
            obj.away = obj_to_rel(teams_objs[partita["away_index"]])
            publish_and_reindex(obj)
    if not api.content.find(portal_type='Video'):
        folder = portal.get("video")
        for video in videos:
            obj = api.content.create(container=folder, type="Video", **video)
            publish_and_reindex(obj)
    if not api.content.find(portal_type='Giocatore'):
        for player in players:
            folder = portal.get("roster")
            player["title"] = player["surname"] + " " + player["name"]
            stats = None
            if "stats" in player:
                stats = player.pop("stats")
            obj = api.content.create(container=folder, type="Giocatore",
                                     **player)
            viola_obj = teams_objs[8]
            obj.team = obj_to_rel(viola_obj)
            if stats:
                _add_subobjs(obj, "stats", "StatisticheGiocatore", stats)
            image_path = os.path.join(base_img_path, "players",
                                      player.pop("image_path"))
            obj.image = load_image(image_path, 'image/jpg')
            image_bg_path = os.path.join(base_img_path, "players",
                                         'players-bg.jpg')
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
            image_path = os.path.join(base_img_path, partner.pop("image"))
            obj = api.content.create(container=folder, type="Partner",
                                     **partner)
            obj.image = load_image(image_path, 'image/png')
            publish_and_reindex(obj)
    if not api.content.find(portal_type='Banner'):
        folder = portal.get("banner")
        for banner in banners:
            image_path = os.path.join(base_img_path, banner.pop("image"))
            obj = api.content.create(container=folder, type="Banner",
                                     **banner)
            obj.image = load_image(image_path, 'image/png')
            publish_and_reindex(obj)
    if not api.content.find(portal_type='Sponsor'):
        folder = portal.get("sponsor")
        for sponsor in sponsors:
            image_path = os.path.join(base_img_path, sponsor.pop("image"))
            obj = api.content.create(container=folder, type="Sponsor",
                                     **sponsor)
            obj.image = load_image(image_path, 'image/png')
            publish_and_reindex(obj)
    if not api.content.find(portal_type='Homepage'):
        obj = api.content.create(container=portal, title="index.html",
                                 type="Homepage", exclude_from_nav=True, )
        obj.slides = [obj_to_rel(s) for s in slides_objs]
        obj.league_hp = get_rel_by_title(leagues_objs, "A2")
        portal.setDefaultPage(obj.id)
        publish_and_reindex(obj)
