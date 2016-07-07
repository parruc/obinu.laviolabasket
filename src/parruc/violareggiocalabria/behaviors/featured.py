# -*- coding: utf-8 -*-
from zope import schema
from zope.component import adapter
from zope.interface import implementer, provider

from plone.app.contenttypes import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model


@provider(IFormFieldProvider)
class IFeatured(model.Schema):

    featured = schema.Bool(
        title=_(u'Mostra in Homepage'),
        description=u"",
        required=False,
    )
    #  model.primary('featured')


@implementer(IFeatured)
@adapter(IDexterityContent)
class Featured(object):

    def __init__(self, context):
        self.context = context
