# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from parruc.violareggiocalabria import _
from plone.app.vocabularies.catalog import CatalogSource
from plone.namedfile.field import NamedBlobFile, NamedBlobImage
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice


class IParrucViolareggiocalabriaLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ISponsor(model.Schema):

    pass


squadre = CatalogSource(path={'query': "/violareggiocalabria/", 'depth': -1},
                        portal_type=("Squadra"))


class ISquadra(model.Schema):

    logo = NamedBlobImage(
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


class IPartita(model.Schema):

    home = RelationChoice(
        title=_("Squadra di casa"),
        source=squadre,
        required=True,
    )

    score_home = schema.Int(
        title=_("Punteggio della squadra di casa"),
        required=False,
    )

    away = RelationChoice(
        title=_("Squadra ospite"),
        source=squadre,
        required=True,
    )

    score_away = schema.Int(
        title=_("Punteggio della squadra in trasferta"),
        required=False,
    )

    start = schema.Datetime(
        title=_("Data ed ora di inizio della partita"),
        required=True,
    )

    league = schema.TextLine(
        title=_("Campionato"),
        default=_("Campionato regolare serie A2"),
    )


class IGiocatore(model.Schema):

    name = schema.TextLine(
        title=_("Nome"),
        required=True,
    )
    surname = schema.TextLine(
        title=_("Cognome"),
        required=True,
    )
    picture = NamedBlobImage(
        title=_(u"Foto"),
        required=True,
    )


class IVideo(model.Schema):

    video = NamedBlobFile(
        title=_("Video"),
        required=True
    )
