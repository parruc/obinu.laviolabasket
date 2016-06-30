# -*- coding: utf-8 -*-

from plone import api
from Products.Five.browser import BrowserView


# from .. import messageFactory as _


class VideoView(BrowserView):

    @property
    def pc(self):
        return api.portal.get_tool(name='portal_catalog')
