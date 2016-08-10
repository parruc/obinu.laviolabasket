# -*- coding: utf-8 -*-
from parruc.violareggiocalabria.utils import get_backrelations
from plone import api
from Products.Five.browser import BrowserView


#  from parruc.violareggiocalabria import _


class GiocatoriView(BrowserView):

    def current_year(self):
        pass

    def get_team(self):
        # TODO: Also query by league
        query = {"portal_type": "Squadra",
                 "is_viola": True, }
        res = api.content.find(**query)
        if len(res) > 0:
            return res[0].getObject()

    def get_players(self):
        team = self.get_team()
        return get_backrelations(team, "team")
