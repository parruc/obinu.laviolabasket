# -*- coding: utf-8 -*-
from collections import OrderedDict
from parruc.devtools import profiled
from Products.Five.browser import BrowserView


#  from parruc.violareggiocalabria import _

class GiocatoreView(BrowserView):
    @profiled(threshold=10)
    def stats(self):
        results = OrderedDict()
        if not self.context.stats:
            return results
        for stat in self.context.stats:
            results[stat.year] = stat
        return results

    @profiled(threshold=10)
    def date_format(self, date):
        day = str(date.day)
        month = str(date.month)
        year = str(date.year)
        return "%s/%s/%s" % (day.zfill(2), month.zfill(2), year)
