# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.namedfile.field import NamedBlobImage
from z3c.relationfield.schema import RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder


from parruc.violareggiocalabria import _


class IParrucViolareggiocalabriaLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ISponsor(Interface):

    pass


class ISquadra(Interface):

    image = NamedBlobImage(
        title=_(u"Logo"),
        required=True,
    )

    played = schema.Int(
        title=_(u"Numero di partite giocatte"),
        required=True,
    )

    points = schema.Int(
        title=_(u"Numero di punti"),
        required=True,
    )

class IPartita(Interface):

    home = RelationChoice(
        title=_("Squadra di casa"),
        source=ObjPathSourceBinder(object_provides=ISquadra.__identifier__),
        required = True,
    )

    away = RelationChoice(
        title=_("Squadra ospite"),
        source=ObjPathSourceBinder(object_provides=ISquadra.__identifier__),
        required = True,
    )

    score_home = schema.Int(
        title = _("Punteggio della squadra di casa"),
        required = False,
    )

    score_away = schema.Int(
        title = _("Punteggio della squadra in trasferta"),
        required = False,
    )

    start = schema.Datetime(
        title=_("Data ed ora di inizio della partita"),
        required = True,
    )

    campionato = schema.TextLine(
        title=_("Campionato"),
        default=_("Campionato regolare serie A2"),
    )

class IGiocatore(Interface):

    nome = schema.TextLine(
        title=_("Nome"),
        required = True,
    )
    cognome = schema.TextLine(
        title=_("Cognome"),
        required = True,
    )
    foto = NamedBlobImage(
        title=_(u"Foto"),
        required=True,
    )
