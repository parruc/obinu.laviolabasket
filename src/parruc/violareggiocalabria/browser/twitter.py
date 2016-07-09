# -*- coding: utf-8 -*-
import logging
import os

import requests

from plone import api
from requests_oauthlib import OAuth1

logger = logging.getLogger("Plone")


class TimelineJsonView(object):
    """Doing it server-side because I'm lazy"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        customer_key = os.getenv("TWITTER_CUSTOMER_KEY", None)
        customer_secret = os.getenv("TWITTER_CUSTOMER_SECRET", None)
        access_token = os.getenv("TWITTER_ACCESS_TOKEN", None)
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", None)
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        params = {"user_id": "993217831", "count": "3"}
        auth = OAuth1(customer_key, customer_secret,
                      access_token, access_token_secret)
        req = requests.get(url, auth=auth, params=params)
        try:
            req.raise_for_status()
            json_data = req.json()
            self.request.response.setHeader("Content-type", "text/json")
            return req.json()
        except Exception as e:
            logger.warning("Falied %s" % str(e))
