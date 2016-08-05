# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView


#  from parruc.violareggiocalabria import _

class GiocatoriView(BrowserView):

    @property
    def pc(self):
        return api.portal.get_tool(name='portal_catalog')

    def current_year(self):
        pass
