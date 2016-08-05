from parruc.violareggiocalabria.content import StatisticheGiocatore
from parruc.violareggiocalabria.content import TeamInLeague
from z3c.form.interfaces import IObjectFactory
from zope.component import adapts
from zope.interface import implements
from zope.interface import Interface


class StatisticheGiocatoreFactory(object):
    adapts(Interface, Interface, Interface, Interface)
    implements(IObjectFactory)

    def __init__(self, context, request, form, widget):
        pass

    def __call__(self, value):
        return StatisticheGiocatore(value)


class TeamInLeagueFactory(object):
    adapts(Interface, Interface, Interface, Interface)
    implements(IObjectFactory)

    def __init__(self, context, request, form, widget):
        pass

    def __call__(self, value):
        return TeamInLeague(value)
