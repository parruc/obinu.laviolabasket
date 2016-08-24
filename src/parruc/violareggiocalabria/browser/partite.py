# -*- coding: utf-8 -*-
from parruc.violareggiocalabria import utils
from Products.Five.browser import BrowserView


#  from parruc.violareggiocalabria import _


class PartiteView(BrowserView):

    def get_team(self):
        league = utils.get_main_league()
        team = league.get_viola()
        return team

    def last_played_match(self):
        team = self.get_team()
        if not team:
            return []
        return team.last_played_match()

    def past_matches(self, limit=5):
        team = self.get_team()
        if not team:
            return []
        return team.past_matches()

    def future_matches(self, limit=5):
        team = self.get_team()
        if not team:
            return []
        matches = team.future_matches()
        if not matches:
            return []
        if len(matches) > limit:
            return matches[:limit]
        return matches

    def format_match_date(self, date):
        return utils.format_date_time(date)

    def format_next_matches_date(self, date):
        return utils.format_date_time(date, month_length=3)

    def get_banners(self, length=1):
        for counter in xrange(length):
            yield utils.get_random_banner()
