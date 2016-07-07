# -*- coding: utf-8 -*-
from zope.component import adapter
from zope.interface import implementer, provider

from plone.app.contenttypes import _
from plone.app.vocabularies.catalog import CatalogSource
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice, RelationList

slides_src = CatalogSource(portal_type=("Slide", ),
                           path={'query': "/violareggiocalabria/",
                                 'depth': -1},)


@provider(IFormFieldProvider)
class ISlider(model.Schema):

    slides = RelationList(title=_(u"Scegli le slide"),
                          default=[],
                          required=False,
                          value_type=RelationChoice(title=_(u"Slide"),
                                                    source=slides_src),
                          )


@implementer(ISlider)
@adapter(IDexterityContent)
class Slider(object):

    def __init__(self, context):
        self.context = context
