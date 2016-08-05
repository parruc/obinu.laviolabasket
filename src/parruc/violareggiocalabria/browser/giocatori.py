# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from plone import api
from Products.Five.browser import BrowserView
from zc.relation.interfaces import ICatalog
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission


#  from parruc.violareggiocalabria import _


def back_references(source_object, attribute_name):
    """ Return back references from source
        object on specified attribute_name """
    pc = getUtility(ICatalog)
    intids = getUtility(IIntIds)
    intid = intids.getId(aq_inner(source_object))
    rels = pc.findRelations(dict(to_id=intid, from_attribute=attribute_name))
    result = []
    for rel in rels:
        obj = intids.queryObject(rel.from_id)
        if obj is not None and checkPermission('zope2.View', obj):
            result.append(obj)
    return result


class GiocatoriView(BrowserView):

    def current_year(self):
        pass

    def get_team(self):
        query = {"portal_type": "Squadra",
                 "Subject": ("viola", "main"), }
        res = api.content.find(**query)
        if len(res) > 0:
            return res[0].getObject()

    def get_players(self):
        team = self.get_team()
        return back_references(team, "team")
