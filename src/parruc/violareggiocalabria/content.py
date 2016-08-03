# -*- coding: utf-8 -*-
from parruc.violareggiocalabria.interfaces import IGiocatore
from parruc.violareggiocalabria.interfaces import IHomepage
from parruc.violareggiocalabria.interfaces import IPartita
from parruc.violareggiocalabria.interfaces import ISponsor
from parruc.violareggiocalabria.interfaces import ISquadra
from parruc.violareggiocalabria.interfaces import IStatisticheGiocatore
from parruc.violareggiocalabria.interfaces import IVideo
from plone.dexterity.content import Item
from zope.interface import implements


class Homepage(Item):
    implements(IHomepage)


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


class Video(Item):
    implements(IVideo)


class StatisticheGiocatore(object):
    implements(IStatisticheGiocatore)

    def __init__(self, values):
        for key, value in values.items():
            setattr(self, key, value)
