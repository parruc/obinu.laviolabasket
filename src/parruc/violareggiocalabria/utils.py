# -*- coding: utf-8 -*-
from datetime import datetime
from DateTime import DateTime
from parruc.violareggiocalabria import _
from plone import api
from zc.relation.interfaces import ICatalog
from zope.component import getUtility
from zope.intid.interfaces import IIntIds

import math


months = [_(u"Gennaio"), _(u"Febbraio"), _(u"Marzo"), _(u"Aprile"),
          _(u"Maggio"), _(u"Giugno"), _(u"Luglio"), _(u"Agosto"),
          _(u"Settembre"), _(u"Ottobre"), _(u"Novembre"), _(u"Dicembre")]


def get_main_league():
    query = {"portal_type": "League", "is_main": True}
    league = api.content.find(**query)
    if len(league) < 1:
        return False
    return league[0].getObject()


def news_link(add=False):
    folder_url = api.portal.get().get("news").absolute_url()
    if add:
        folder_url += "/++add++News Item"
    return folder_url


def roster_link(add=False):
    folder_url = api.portal.get().get("roster").absolute_url()
    if add:
        folder_url += "/++add++Giocatore"
    return folder_url


def giocatori_link(add=False):
    return roster_link(add)


def video_link(add=False):
    folder_url = api.portal.get().get("video").absolute_url()
    if add:
        folder_url += "/++add++Video"
    return folder_url


def partite_link(add=False):
    folder_url = api.portal.get().get("partite").absolute_url()
    if add:
        folder_url += "/++add++Partita"
    return folder_url


def squadre_link(add=False):
    folder_url = api.portal.get().get("squadre").absolute_url()
    if add:
        folder_url += "/++add++Squadra"
    return folder_url


def format_date_ago(date):
    if isinstance(date, DateTime):
        date = date.asdatetime()
    now = datetime.now()
    if getattr(date, "tzinfo", None):
        now = (now + date.utcoffset()).replace(tzinfo=date.tzinfo)
    since = now - date
    seconds = since.seconds + since.days * 86400
    days = math.floor(seconds / (3600*24))
    if days <= 0:
        return _(u"oggi")
    if days == 1:
        return _(u"ieri")
    if days < 7:
        return _(u"%d giorni fa" % days)
    if days < 30:
        week = _(u"settimane")
        if days < 14:
            week = _(u"settimana")
        weeks = math.floor(days / 7)
        return _(u"%d %s fa" % (weeks, week))
    if days < 365:
        month = _(u"mesi")
        if days < 60:
            week = _(u"mese")
        months = math.floor(days / 30)
        return _(u"%d %s fa" % (months, month))
    else:
        year = _(u"anni")
        if days < 730:
            year = _("anno")
        years = math.floor(days / 365)
        return _(u"%d %s fa" % (years, year))


def format_date(date, month_length=0):
    if isinstance(date, DateTime):
        date = date.asdatetime()
    day = str(date.day).zfill(2)
    month = months[date.month-1]
    if month_length:
        month = month[:month_length]
    return "%s %s" % (day, month)


def format_date_time(date, month_length=0):
    if isinstance(date, DateTime):
        date = date.asdatetime()
    day = str(date.day).zfill(2)
    month = months[date.month-1]
    if month_length:
        month = month[:month_length]
    hour = str(date.hour).zfill(2)
    minute = str(date.minute).zfill(2)
    return "%s %s %s:%s" % (day, month, hour, minute)


def get_relations(obj, attribute=None, backrefs=False):
    """Get any kind of references and backreferences"""
    retval = []
    int_id = get_intid(obj)
    if not int_id:
        return retval

    relation_catalog = getUtility(ICatalog)
    if not relation_catalog:
        return retval

    query = {}
    if attribute:
        # Constrain the search for certain relation-types.
        query['from_attribute'] = attribute

    if backrefs:
        query['to_id'] = int_id
    else:
        query['from_id'] = int_id
    relations = relation_catalog.findRelations(query)
    for relation in relations:
        if relation.isBroken():
            continue
        retval.append(relation)
    return retval


def get_backrelations(obj, attribute=None):
    return get_relations(obj, attribute=attribute, backrefs=True)


def get_intid(obj):
    """Return the intid of an object from the intid-catalog"""
    intids = getUtility(IIntIds)
    if intids is None:
        return
    # check that the object has an intid, otherwise there's nothing to be done
    try:
        return intids.getId(obj)
    except KeyError:
        # The object has not been added to the ZODB yet
        return
