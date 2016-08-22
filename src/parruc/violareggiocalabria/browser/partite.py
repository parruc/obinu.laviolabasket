# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView


#  from parruc.violareggiocalabria import _


class PartiteView(BrowserView):

    def get_team(self):
        query = {"portal_type": "League", "is_main": True}
        league = api.content.find(**query)[0].getObject()
        team = league.get_viola()
        return team

    def last_played_match(self):
        team = self.context.league_hp.to_object.get_viola()
        if not team:
            return []
        return team.last_played_match()

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
