# -*- coding: utf-8 -*-
#  from plone.memoize import view
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
from parruc.violareggiocalabria.utils import get_backrelations
from parruc.violareggiocalabria.vocabularies import match_types
from parruc.violareggiocalabria.vocabularies import video_categories
from plone.dexterity.content import Item
from zope.interface import implements


class Homepage(Item):
    implements(IHomepage)


class League(Item):
    implements(ILeague)

    #  @view.memoize
    def get_teams(self):
        """ TODO: Trasformare in view così posso cachare """
        return [r.from_object for r in get_backrelations(self, "league")]

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

    def get_match_type_title(self):
        if not getattr(self, "match_type", None):
            return ""
        return match_types.getTerm(self.match_type).title


class Sponsor(Item):
    implements(ISponsor)


class Partner(Item):
    implements(ISponsor)


class Squadra(Item):
    implements(ISquadra)

    def get_players(self):
        return [r.from_object for r in get_backrelations(self, "team")]

    #  @view.memoize
    def get_matches(self):
        home = [r.from_object for r in get_backrelations(self, "home")]
        away = [r.from_object for r in get_backrelations(self, "away")]
        matches = home + away
        matches.sort(key=lambda match: match.start, reverse=False)
        return matches

    def last_played_match(self):
        now = datetime.now()
        matches = self.get_matches()
        matches.reverse()
        for match in matches:
            if match.start < now and match.score_home and match.score_away:
                return match

    def future_matches(self):
        results = []
        now = datetime.now()
        matches = self.get_matches()
        for match in matches:
            if match.start > now:
                results.append(match)
        return results

    def past_matches(self):
        results = []
        now = datetime.now()
        matches = self.get_matches()
        for match in matches:
            if match.start < now:
                results.append(match)
        return results


class Video(Item):
    implements(IVideo)

    def get_video_category_title(self):
        if not getattr(self, "video_category", None):
            return ""
        return video_categories.getTerm(self.video_category).title


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
