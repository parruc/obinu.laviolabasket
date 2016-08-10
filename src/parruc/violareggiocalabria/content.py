# -*- coding: utf-8 -*-
from datetime import datetime
from parruc.violareggiocalabria.interfaces import IGiocatore
from parruc.violareggiocalabria.interfaces import IHomepage
from parruc.violareggiocalabria.interfaces import ILeague
from parruc.violareggiocalabria.interfaces import IPartita
from parruc.violareggiocalabria.interfaces import ISponsor
from parruc.violareggiocalabria.interfaces import ISquadra
from parruc.violareggiocalabria.interfaces import IStatisticheGiocatore
from parruc.violareggiocalabria.interfaces import ITeamInLeague
from parruc.violareggiocalabria.interfaces import IVideo
from parruc.violareggiocalabria.utils import back_references
from plone.dexterity.content import Item
#  from plone.memoize import view
from zope.interface import implements


class Homepage(Item):
    implements(IHomepage)


class League(Item):
    implements(ILeague)

    #  @view.memoize
    def get_teams(self):
        return back_references(self, "league")

    #  @view.memoize
    def get_viola(self):
        for team in self.get_teams():
            if team.is_viola:
                return team
        return False


class Giocatore(Item):
    implements(IGiocatore)


class Partita(Item):
    implements(IPartita)


class Sponsor(Item):
    implements(ISponsor)


class Partner(Item):
    implements(ISponsor)


class Squadra(Item):
    implements(ISquadra)

    def get_players(self):
        return back_references(self, "team")

    #  @view.memoize
    def get_matches(self):
        home = back_references(self, "home")
        away = back_references(self, "away")
        matches = home + away
        matches.sort(lambda match: match.start)
        return matches

    def last_played_match(self):
        now = datetime.now()
        matches = self.get_matches()
        matches.reverse()
        for match in matches:
            if match.start < now and match.score_home and match.score_away:
                return match

    def future_matches(self):
        now = datetime.now()
        matches = self.get_matches()
        for match in matches:
            if match.start > now:
                yield match


class Video(Item):
    implements(IVideo)


class StatisticheGiocatore(object):
    implements(IStatisticheGiocatore)

    def __init__(self, **values):
        for key, value in values.items():
            setattr(self, key, value)


class TeamInLeague(object):
    implements(ITeamInLeague)

    def __init__(self, **values):
        for key, value in values.items():
            setattr(self, key, value)
