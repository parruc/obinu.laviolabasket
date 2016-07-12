# -*- coding: utf-8 -*-
from datetime import datetime

from parruc.violareggiocalabria import _

base_perm = "parruc.violareggiocalabria: Add "


folders = [{"title": _("Partite"), "permission": base_perm + "Partita",
            "exclude_from_nav": False},
           {"title": _("Roster"), "permission": base_perm + "Giocatore",
            "exclude_from_nav": False},
           {"title": _("News"), "permission": base_perm + "News Item",
            "exclude_from_nav": False},
           {"title": _("Sponsor"), "permission": base_perm + "Sponsor",
            "exclude_from_nav": True},
           {"title": _("Partner"), "permission": base_perm + "Partner",
            "exclude_from_nav": True},
           {"title": _("Squadre"), "permission": base_perm + "Squadra",
            "exclude_from_nav": True},
           {"title": _("Video"), "permission": base_perm + "Video",
            "exclude_from_nav": True},
           {"title": _("Slides"), "permission": base_perm + "Slide",
            "exclude_from_nav": True}, ]

pages = [{"title": _("Team")},
         {"title": _("Storia")},
         {"title": _("Club")},
         {"title": _("Pala Calafiore")},
         {"title": _("Contatti")}, ]

teams = [{"title": "Givova Scafati", "played": 30, "points": 40,
          "image_logo": "loghi/givova-scafati.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "BCC Agropoli", "played": 30, "points": 38,
          "image_logo": "loghi/bcc-agropoli.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "Orsi Tortona", "played": 30, "points": 38,
          "image_logo": "loghi/orsi-tortona.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "FMC Ferentino", "played": 30, "points": 36,
          "image_logo": "loghi/mfc-ferentino.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "Mens Sana Basket 1871 Siena", "played": 30, "points": 36,
          "image_logo": "loghi/menssana-siena.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "Moncada Agrigento", "played": 30, "points": 34,
          "image_logo": "loghi/moncada-agrigento.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "Lighthouse Conad Trapani", "played": 30, "points": 32,
          "image_logo": "loghi/lighthouseconad-trapani.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "Novipiù Casale Monferrato", "played": 30, "points": 30,
          "image_logo": "loghi/novapiu-casale.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "Bermé Reggio Calabria", "played": 30, "points": 28,
          "image_logo": "loghi/viola-reggiocalabria.png",
          "image_teaser": "teaser2.jpg"},
         {"title": "Angelico Biella", "played": 30, "points": 28,
          "image_logo": "loghi/angelico-biella.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "Assigeco Casalpusterlengo", "played": 30, "points": 26,
          "image_logo": "loghi/assigeco-casalpusterlengo.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "Benacquista Ass. Latina", "played": 30, "points": 26,
          "image_logo": "loghi/nologo.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "Npc Rieti", "played": 30, "points": 26,
          "image_logo": "loghi/npc-rieti.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "Acea Roma", "played": 30, "points": 26,
          "image_logo": "loghi/acea-roma.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "Paffoni Omegna", "played": 30, "points": 24,
          "image_logo": "loghi/paffoni-omegna.png",
          "image_teaser": "teaser1.jpg"},
         {"title": "La Briosa Barcellona", "played": 30, "points": 12,
          "image_logo": "loghi/briosa-barcellona.png",
          "image_teaser": "teaser1.jpg"}, ]


partite = [{"title": "Vittoria al cardiopalma",
            "home_index": 8, "away_index": 5,
            "score_home": 100, "score_away": 99,
            "start": datetime(2016, 7, 1, 15, 30, 0), },
           {"title": "Vittoria al cardiopalma",
            "home_index": 8, "away_index": 9,
            "score_home": 100, "score_away": 99,
            "start": datetime(2016, 8, 1, 15, 30, 0), },
           {"title": "Grande vittoria fuori casa",
            "home_index": 2, "away_index": 8,
            "score_home": 45, "score_away": 100,
            "start": datetime(2016, 9, 1, 19, 30, 0), },
           {"title": "Sconfitta di misura",
            "home_index": 1, "away_index": 8,
            "score_home": 98, "score_away": 110,
            "start": datetime(2016, 10, 1, 21, 30, 0), }, ]

slides = [{"title": "La viola mette a segno punti preziosi",
           "url": "/",
           "image": "slide1.jpg"},
          {"title": "Un'altra vittoria per i ragazzi della Viola",
           "url": "/",
           "image": "slide2.jpg"}, ]

videos = [{"title": "Coach Frates post Viola Tortona",
           "url": "https://www.youtube.com/embed/BFTz_-bIVuM"},
          {"title": "Valerio Costa post Viola Casalpusterlengo",
          "url": "https://www.youtube.com/embed/18Op_UYJEYw"},
          {"title": "Coach Bolignano post Viola Trapani",
           "url": "https://www.youtube.com/embed/YjnDyeSrgYo"},
          {"title": "Roberto Rullo post Viola Trapani",
           "url": "https://www.youtube.com/embed/rzlLYloWQpM"}
          ]
players = [{"name": "Ion", "surname": "Lupusor", "role": "Ala"},
           {"name": "Lorenzo", "surname": "Caroti", "role": "Playmaker"},
           {"name": "Tommaso", "surname": "Guariglia", "role": "Cenntro"},
           {"name": "Celis", "surname": "Taflaj", "role": "Guardia"}, ]

news = [{"title": "News diprova 1",
         "description": "Questa è una news di prova"},
        {"title": "News diprova 2",
         "description": "Questa è una news di prova"},
        {"title": "News diprova 3",
         "description": "Questa è una news di prova"},
        {"title": "News diprova 4",
         "description": "Questa è una news di prova"},
        {"title": "News diprova 5", "description":
         "Questa è una news di prova"}, ]

partners = [{"title": "Partner 1", "image": "loghi/viola-reggiocalabria.png"},
            {"title": "Partner 2", "image": "loghi/viola-reggiocalabria.png"},
            {"title": "Partner 3", "image": "loghi/viola-reggiocalabria.png"}]

sponsors = [{"title": "Sponsor 1", "image": "loghi/viola-reggiocalabria.png"},
            {"title": "Sponsor 2", "image": "loghi/viola-reggiocalabria.png"},
            {"title": "Sponsor 3", "image": "loghi/viola-reggiocalabria.png"}]
