# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView


#  from parruc.violareggiocalabria import _


class GiocatoriView(BrowserView):

    def get_players(self):
        query = {"portal_type": "League", "is_main": True}
        league = api.content.find(**query)[0].getObject()
        team = league.get_viola()
        return team.get_players()
