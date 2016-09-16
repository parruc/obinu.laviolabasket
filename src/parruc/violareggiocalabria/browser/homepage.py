# -*- coding: utf-8 -*-
# from plone.memoize import view
from datetime import datetime
from parruc.devtools import profiled
from parruc.violareggiocalabria import utils
from plone import api
from plone.memoize import ram
from Products.Five.browser import BrowserView
from requests_oauthlib import OAuth1
from time import time

import logging
import os
import requests


# from .. import messageFactory as _
logger = logging.getLogger("Plone")


class HomepageView(BrowserView):
    @profiled(threshold=10)
    def last_played_match(self):
        team = self.context.league_hp.to_object.get_viola()
        if not team:
            return []
        return team.last_played_match()

    @profiled(threshold=10)
    def future_matches(self, limit=5):
        team = self.context.league_hp.to_object.get_viola()
        if not team:
            return []
        matches = team.future_matches()
        if not matches:
            return []
        if len(matches) > limit:
            return matches[:limit]
        return matches

    @profiled(threshold=10)
    def next_match_datetime(self):
        next_match = self.future_matches(limit=1)
        if next_match:
            return next_match[0].start.strftime("%Y/%m/%d %H:%M:%S")

    @profiled(threshold=10)
    def latest_videos(self, limit=4):
        query = {"portal_type": "Video",
                 "sort_on": "getObjPositionInParent",
                 "sort_limit": limit}
        return [b.getObject() for b in api.content.find(**query)[:limit]]

    @profiled(threshold=10)
    def players(self):
        team = self.context.league_hp.to_object.get_viola()
        return team.get_players()

    @profiled(threshold=10)
    def latest_news(self, limit=5):
        """ TODO: get only featured"""
        query = {"portal_type": "News Item",
                 "sort_on": "effective",
                 "sort_limit": limit, }
        return api.content.find(**query)[:limit]

    @profiled(threshold=10)
    def partners(self, limit=6):
        query = {"portal_type": "Partner",
                 "sort_on": "getObjPositionInParent",
                 "sort_limit": limit, }
        return [b.getObject() for b in api.content.find(**query)[:limit]]

    @profiled(threshold=10)
    def sponsors(self, limit=6):
        query = {"portal_type": "Sponsor",
                 "sort_on": "getObjPositionInParent",
                 "sort_limit": limit, }
        return [b.getObject() for b in api.content.find(**query)[:limit]]

    @profiled(threshold=10)
    def classifica(self):
        query = {"portal_type": "Squadra",
                 "sort_on": "points",
                 "sort-order": "descending", }
        return api.content.find(**query)

    @profiled(threshold=10)
    @ram.cache(lambda *args: time() // (60 * 10))
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
            format = '%a %b %d %H:%M:%S +0000 %Y'
            created = datetime.strptime(item['created_at'], format)
            urls = []
            if "entities" in item and "urls" in item["entities"]:
                urls += item["entities"]["urls"]
            if "entities" in item and "media" in item["entities"]:
                urls += item["entities"]["media"]
            for url in urls:
                u = url["url"]
                text = text.replace(u, "<a href='"+u+"'>"+u+"</a>")
            name = item["user"]["screen_name"]
            results.append({"text": text, "name": name, "created": created})

        return results

    @profiled(threshold=10)
    def format_news_date(self, date):
        return utils.format_date(date, month_length=3)

    @profiled(threshold=10)
    def format_match_date(self, date):
        return utils.format_date_time(date)

    @profiled(threshold=10)
    def format_next_matches_date(self, date):
        return utils.format_date_time(date, month_length=3)

    @profiled(threshold=10)
    def format_video_date(self, date):
        return utils.format_date_ago(date)

    @profiled(threshold=10)
    def format_twitter_date(self, date):
        return utils.format_date_ago(date)

    @profiled(threshold=10)
    def news_link(self):
        return utils.news_link()

    @profiled(threshold=10)
    def roster_link(self):
        return utils.roster_link()

    @profiled(threshold=10)
    def video_link(self):
        return utils.video_link()
