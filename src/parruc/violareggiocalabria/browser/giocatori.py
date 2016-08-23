# -*- coding: utf-8 -*-
from parruc.violareggiocalabria import utils
from Products.Five.browser import BrowserView


#  from parruc.violareggiocalabria import _


class GiocatoriView(BrowserView):

    def get_players(self):
        league = utils.get_main_league()
        team = league.get_viola()
        return team.get_players()
