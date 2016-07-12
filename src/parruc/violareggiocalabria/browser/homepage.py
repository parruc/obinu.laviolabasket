# -*- coding: utf-8 -*-
import logging
import os
from datetime import datetime

import requests

from plone import api
from Products.Five.browser import BrowserView
from requests_oauthlib import OAuth1

# from .. import messageFactory as _
logger = logging.getLogger("Plone")

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

    def latest_videos(self, limit=4):
        query = {"portal_type": "Video",
                 "sort_on": "getObjPositionInParent",
                 "sort_limit": limit}
        return [b.getObject() for b in api.content.find(**query)[:limit]]

    def players(self):
        """ TODO: replace con references in hp"""
        query = {"portal_type": "Giocatore",
                 "sort_on": "getObjPositionInParent", }
        return [b.getObject() for b in api.content.find(**query)]

    def latest_news(self, limit=5):
        """ TODO: get only featured"""
        query = {"portal_type": "News Item",
                 "sort_on": "effective",
                 "sort_limit": limit, }
        return [b.getObject() for b in api.content.find(**query)[:limit]]

    def partners(self, limit=6):
        query = {"portal_type": "Partner",
                 "sort_on": "getObjPositionInParent",
                 "sort_limit": limit, }
        return [b.getObject() for b in api.content.find(**query)[:limit]]

    def sponsors(self, limit=6):
        query = {"portal_type": "Sponsor",
                 "sort_on": "getObjPositionInParent",
                 "sort_limit": limit, }
        return [b.getObject() for b in api.content.find(**query)[:limit]]

    def classifica(self):
        query = {"portal_type": "Squadra",
                 "sort_on": "points",
                 "sort-order": "descending", }
        return api.content.find(**query)

    def format_news_date(self, zope_date):
        short_months = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug",
                        "Ago", "Set", "Ott", "Nov", "Dic"]
        date = zope_date.asdatetime()
        return "%d %s" % (date.day, short_months[date.month-1])

    def news_link(self):
        return api.portal.get().get("news").absolute_url()

    def team_link(self):
        return api.portal.get().get("team").absolute_url()

    def tweets(self):
        customer_key = os.getenv("TWITTER_CUSTOMER_KEY", None)
        customer_secret = os.getenv("TWITTER_CUSTOMER_SECRET", None)
        access_token = os.getenv("TWITTER_ACCESS_TOKEN", None)
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", None)
        if not(customer_key and customer_secret and
               access_token and access_token):
            logger.warning("Missing Twitter global vars")
            return[]
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        params = {"user_id": "993217831", "count": "3"}
        auth = OAuth1(customer_key, customer_secret,
                      access_token, access_token_secret)
        results = []
        try:
            req = requests.get(url, auth=auth, params=params, timeout=1)
            req.raise_for_status()
            json_data = req.json()
        except Exception as e:
            logger.warning("Falied %s" % str(e))
            return[]
        for item in json_data:
            text = item["text"]
            urls = []
            if "entities" in item and "urls" in item["entities"]:
                urls += item["entities"]["urls"]
            if "entities" in item and "media" in item["entities"]:
                urls += item["entities"]["media"]
            for url in urls:
                u = url["url"]
                text = text.replace(u, "<a href='"+u+"'>"+u+"</a>")
            name = item["user"]["screen_name"]
            results.append({"text": text, "name": name})

        return results
