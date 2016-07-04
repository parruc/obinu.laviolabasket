# -*- coding: utf-8 -*-

from datetime import datetime

from plone import api
from Products.Five.browser import BrowserView


# from .. import messageFactory as _


class HomepageView(BrowserView):

    @property
    def pc(self):
        return api.portal.get_tool(name='portal_catalog')

    def last_played_match(self):
        now = datetime.now()
        query = {"portal_type": "Partita",
                 "start":{'query':[now],'range':'max'},
                 "sort_on":"start",
                 "sort_order":"descending",
                 "sort_limit":5}
        matches = self.pc.searchResults(query)
        for match in matches:
            if match["score_home"] and match["score_away"]:
                return match

    def future_matches(self,limit=5):
        now = datetime.now()
        query = {"portal_type": "Partita",
                 "start":{'query':[now],'range':'min'},
                 "sort_on":"start",
                 "sort_order":"ascending",
                 "sort_limit":limit}
        return self.pc.searchResults(query)[:limit]

    def next_match_datetime(self):
        import ipdb; ipdb.set_trace()
        next_match = self.future_matches(1)[0]
        return next_match["start"].strftime("%Y/%m/%d %H:%M:%S")
