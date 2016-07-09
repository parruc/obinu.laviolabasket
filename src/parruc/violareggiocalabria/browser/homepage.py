# -*- coding: utf-8 -*-

import locale
from datetime import datetime

from plone import api
from Products.Five.browser import BrowserView


# from .. import messageFactory as _


class HomepageView(BrowserView):

    def last_played_match(self):
        now = datetime.now()
        query = {"portal_type": "Partita",
                 "start": {'query': [now], 'range': 'max'},
                 "sort_on": "start",
                 "sort_order": "descending",
                 "sort_limit": 5}
        matches = api.content.find(**query)
        for match in matches:
            if match["score_home"] and match["score_away"]:
                return match

    def future_matches(self, limit=5):
        now = datetime.now()
        query = {"portal_type": "Partita",
                 "start": {'query': [now], 'range': 'min'},
                 "sort_on": "start",
                 "sort_order": "ascending",
                 "sort_limit": limit}
        return api.content.find(**query)[:limit]

    def next_match_datetime(self):
        next_match = self.future_matches(limit=1)
        if next_match:
            return next_match[0]["start"].strftime("%Y/%m/%d %H:%M:%S")

    def latest_videos(self, limit=5):
        query = {"portal_type": "Video",
                 "sort_on": "getObjPositionInParent",
                 "sort_limit": limit}
        return [b.getObject() for b in api.content.find(**query)[:limit]]

    def players(self):
        query = {"portal_type": "Giocatore",
                 "sort_on": "getObjPositionInParent", }
        return [b.getObject() for b in api.content.find(**query)]

    def latest_news(self, limit=5):
        query = {"portal_type": "News Item",
                 "sort_on": "effective",
                 "sort_limit": limit,}
        return [b.getObject() for b in api.content.find(**query)[:limit]]

    def format_news_date(self, zope_date):
        short_months = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug",
                        "Ago", "Set", "Ott", "Nov", "Dic"]
        date = zope_date.asdatetime()
        return "%d %s" % (date.day, short_months[date.month-1])

    def news_link(self):
        """ TODO: get only featured"""
        return api.portal.get().get("notizie").absolute_url()

    def team_link(self):
        """ TODO: replace con references in hp"""
        return api.portal.get().get("giocatori").absolute_url()
