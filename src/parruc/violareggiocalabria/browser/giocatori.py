# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView


#  from parruc.violareggiocalabria import _


class GiocatoriView(BrowserView):

    def current_year(self):
        pass

    def get_players(self):
        query = {"portal_type": "Homepage", "sort_limit": 1}
        hp = api.content.find(**query)[0].getObject()
        team = hp.league_hp.to_object.get_viola()
        return team.get_players()
