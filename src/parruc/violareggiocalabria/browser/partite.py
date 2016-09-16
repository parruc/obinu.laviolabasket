# -*- coding: utf-8 -*-
from parruc.devtools import profiled
from parruc.violareggiocalabria import utils
from Products.Five.browser import BrowserView


#  from parruc.violareggiocalabria import _


class PartiteView(BrowserView):
    @profiled(threshold=10)
    def get_team(self):
        league = utils.get_main_league()
        team = league.get_viola()
        return team

    @profiled(threshold=10)
    def last_played_match(self):
        team = self.get_team()
        if not team:
            return []
        return team.last_played_match()

    @profiled(threshold=10)
    def past_matches(self, limit=5):
        team = self.get_team()
        if not team:
            return []
        return team.past_matches()

    @profiled(threshold=10)
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

    @profiled(threshold=10)
    def format_match_date(self, date):
        return utils.format_date_time(date)

    @profiled(threshold=10)
    def format_next_matches_date(self, date):
        return utils.format_date_time(date, month_length=3)

    @profiled(threshold=10)
    def next_match_datetime(self):
        next_match = self.future_matches(limit=1)
        if next_match:
            return next_match[0].start.strftime("%Y/%m/%d %H:%M:%S")
