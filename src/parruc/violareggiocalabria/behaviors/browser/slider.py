# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import common as base


class SliderViewlet(base.ViewletBase):

    @property
    def pc(self):
        return api.portal.get_tool(name='portal_catalog')

    def slides(self):
        return self.context.slides
