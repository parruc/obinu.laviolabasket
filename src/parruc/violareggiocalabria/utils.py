# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from zc.relation.interfaces import ICatalog
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission


def back_references(source_object, attribute_name):
    """ Return back references from source
        object on specified attribute_name """
    catalog = getUtility(ICatalog)
    intids = getUtility(IIntIds)
    result = []
    for rel in catalog.findRelations(
        dict(to_id=intids.getId(aq_inner(source_object)),
             from_attribute=attribute_name)):
        obj = intids.queryObject(rel.from_id)
        if obj is not None and checkPermission('zope2.View', obj):
            result.append(obj)
    return result
