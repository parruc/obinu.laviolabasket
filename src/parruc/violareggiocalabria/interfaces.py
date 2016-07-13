# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope import schema
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from parruc.violareggiocalabria import _
from parruc.violareggiocalabria.vocabularies import launches, teams
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from plone.supermodel.directives import primary
from z3c.relationfield.schema import RelationChoice


class IParrucViolareggiocalabriaLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
    pass


class ISponsor(model.Schema):

    link = schema.URI(
        title=_("Link al sito dello sponsor"),
        required=True
    )


class IPartner(model.Schema):

    pass


class IHomepage(model.Schema):

    launch = RelationChoice(
        title=_(u"Lancio ad una pagina o notizia"),
        description=_(u"Sostituisce il risultato dell'ultima partita"),
        source=launches,
        required=False,
    )

    launch_image = NamedBlobImage(
        title=_(u"Immagine per il lancio"),
        required=True,
    )


class ISquadra(model.Schema):

    image_logo = NamedBlobImage(
        title=_(u"Logo"),
        required=True,
    )

    image_teser = NamedBlobImage(
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
        title=_(u"Squadra di casa"),
        source=teams,
        required=True,
    )

    score_home = schema.Int(
        title=_(u"Punteggio della squadra di casa"),
        required=False,
    )

    away = RelationChoice(
        title=_("Squadra ospite"),
        source=teams,
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
    role = schema.TextLine(
        title=_("Ruolo"),
        required=True,
    )
    image = NamedBlobImage(
        title=_(u"Foto"),
        required=True,
    )


class IVideo(model.Schema):

    url = schema.URI(
        title=_("Url del video youtube"),
        required=True
    )
