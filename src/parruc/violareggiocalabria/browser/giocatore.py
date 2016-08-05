# -*- coding: utf-8 -*-
from collections import OrderedDict
from plone import api
from Products.Five.browser import BrowserView


#  from parruc.violareggiocalabria import _

class GiocatoreView(BrowserView):

    def stats(self):
        results = OrderedDict()
        if not self.context.stats:
            return results
        for stat in self.context.stats:
            results[stat.year] = stat
        return results
