# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from parruc.violareggiocalabria import _
from parruc.violareggiocalabria.vocabularies import launches
from parruc.violareggiocalabria.vocabularies import leagues
from parruc.violareggiocalabria.vocabularies import teams
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IParrucViolareggiocalabriaLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
    pass


class ISponsor(model.Schema):

    link = schema.URI(
        title=_("Link al sito dello sponsor"),
        required=True
    )


class ITeamInLeague(Interface):

        played = schema.Int(
            title=_(u"Numero di partite giocate"),
            required=True,
        )

        points = schema.Int(
            title=_(u"Numero di punti"),
            required=True,
        )
        team = RelationChoice(
            title=_(u"Team"),
            required=True,
            source=launches,
        )


class ILeague(model.Schema):

    teams = schema.List(
        title=_(u"Teams"),
        required=False,
        value_type=schema.Object(title=_("Squadra"),
                                 schema=ITeamInLeague),
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

    league = RelationChoice(
        title=_(u"Campionato a cui partecipa"),
        source=leagues,
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

    league = RelationChoice(
        title=_(u"Campionato a cui partecipa"),
        source=leagues,
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


class IStatisticheGiocatore(Interface):

        year = schema.TextLine(
            title=_("Anno di riferimento"),
            required=True,
        )

        played = schema.Int(
            title=_(u"Numero di partite giocate"),
            required=True,
        )

        score = schema.Int(
            title=_(u"Punti fatti"),
            required=True,
        )

        played_time = schema.Int(
            title=_(u"Minuti giocati"),
            required=True,
        )

        two_points_shots = schema.Int(
            title=_(u"Tiri da due"),
            required=True,
        )

        two_points_shots_percent = schema.Int(
            title=_(u"Percentuale da due"),
            required=True,
        )

        three_points_shots = schema.Int(
            title=_(u"Tiri da tre"),
            required=True,
        )

        three_points_shots_percent = schema.Int(
            title=_(u"Percentuale da tre"),
            required=True,
        )

        rebounds = schema.Int(
            title=_(u"Rimbalzi"),
            required=True,
        )

        blocked = schema.Int(
            title=_(u"Stoppate"),
            required=True,
        )


class IGiocatore(model.Schema):

    name = schema.TextLine(
        title=_(u"Nome"),
        required=True,
    )
    surname = schema.TextLine(
        title=_(u"Cognome"),
        required=True,
    )
    birth_date = schema.Date(
        title=_(u"Data di nascita"),
        required=True,

    )
    role = schema.TextLine(
        title=_(u"Ruolo"),
        required=True,
    )
    image = NamedBlobImage(
        title=_(u"Foto"),
        required=True,
    )

    image_back = NamedBlobImage(
        title=_(u"Foto di sfondo"),
        required=True,
    )

    height = schema.Int(
        title=_(u"Altezza in cm"),
        required=True,
    )

    weight = schema.Int(
        title=_(u"Peso in kg"),
    )

    stats = schema.List(
        title=_(u"Statistiche"),
        required=False,
        value_type=schema.Object(title=_("Statistiche stagionali"),
                                 schema=IStatisticheGiocatore),

    )


class IVideo(model.Schema):

    url = schema.URI(
        title=_("Url del video youtube"),
        required=True
    )
