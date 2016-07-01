# -*- coding: utf-8 -*-
from zope.interface import implements

from parruc.violareggiocalabria.interfaces import (IGiocatore, IPartita,
                                                   ISponsor, ISquadra, IVideo)
from plone.dexterity.content import Item


class Giocatore(Item):
    implements(IGiocatore)


class Partita(Item):
    implements(IPartita)


class Sponsor(Item):
    implements(ISponsor)


class Squadra(Item):
    implements(ISquadra)


class Video(Item):
    implements(IVideo)
