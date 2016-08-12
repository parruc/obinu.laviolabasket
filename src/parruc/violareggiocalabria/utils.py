# -*- coding: utf-8 -*-
from zc.relation.interfaces import ICatalog
from zope.component import getUtility
from zope.intid.interfaces import IIntIds


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
