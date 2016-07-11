# -*- coding: utf-8 -*-
from datetime import datetime

from parruc.violareggiocalabria import _

base_perm = "parruc.violareggiocalabria: Add "


folders = [{"title": _("Giocatori"), "permission": base_perm + "Giocatore",
            "exclude_from_nav": True},
           {"title": _("Notizie"), "permission": base_perm + "News Item",
            "exclude_from_nav": False},
           {"title": _("Partite"), "permission": base_perm + "Partita",
            "exclude_from_nav": True},
           {"title": _("Sponsor"), "permission": base_perm + "Sponsor",
            "exclude_from_nav": True},
           {"title": _("Squadre"), "permission": base_perm + "Squadra",
            "exclude_from_nav": True},
           {"title": _("Video"), "permission": base_perm + "Video",
            "exclude_from_nav": True},
           {"title": _("Slides"), "permission": base_perm + "Slide",
            "exclude_from_nav": True}, ]


teams = [{"title": "Givova Scafati", "played": 30, "points": 40,
          "logo": "loghi/givova-scafati.png"},
         {"title": "BCC Agropoli", "played": 30, "points": 38,
          "logo": "loghi/bcc-agropoli.png"},
         {"title": "Orsi Tortona", "played": 30, "points": 38,
          "logo": "loghi/orsi-tortona.png"},
         {"title": "FMC Ferentino", "played": 30, "points": 36,
          "logo": "loghi/mfc-ferentino.png"},
         {"title": "Mens Sana Basket 1871 Siena", "played": 30, "points": 36,
          "logo": "loghi/menssana-siena.png"},
         {"title": "Moncada Agrigento", "played": 30, "points": 34,
         "logo": "loghi/moncada-agrigento.png"},
         {"title": "Lighthouse Conad Trapani", "played": 30, "points": 32,
          "logo": "loghi/lighthouseconad-trapani.png"},
         {"title": "Novipiù Casale Monferrato", "played": 30, "points": 30,
          "logo": "loghi/novapiu-casale.png"},
         {"title": "Bermé Reggio Calabria", "played": 30, "points": 28,
          "logo": "loghi/viola-reggiocalabria.png"},
         {"title": "Angelico Biella", "played": 30, "points": 28,
          "logo": "loghi/angelico-biella.png"},
         {"title": "Assigeco Casalpusterlengo", "played": 30, "points": 26,
          "logo": "loghi/assigeco-casalpusterlengo.png"},
         {"title": "Benacquista Ass. Latina", "played": 30, "points": 26,
          "logo": "loghi/nologo.png"},
         {"title": "Npc Rieti", "played": 30, "points": 26,
          "logo": "loghi/npc-rieti.png"},
         {"title": "Acea Roma", "played": 30, "points": 26,
          "logo": "loghi/acea-roma.png"},
         {"title": "Paffoni Omegna", "played": 30, "points": 24,
          "logo": "loghi/paffoni-omegna.png"},
         {"title": "La Briosa Barcellona", "played": 30, "points": 12,
          "logo": "loghi/briosa-barcellona.png"}, ]


partite = [{"title": "Vittoria al cardiopalma",
            "home_index": 9, "away_index": 5,
            "score_home": 100, "score_away": 99,
            "start": datetime(2016, 7, 1, 15, 30, 0), },
           {"title": "Vittoria al cardiopalma",
            "home_index": 9, "away_index": 8,
            "score_home": 100, "score_away": 99,
            "start": datetime(2016, 8, 1, 15, 30, 0), },
           {"title": "Grande vittoria fuori casa",
            "home_index": 2, "away_index": 9,
            "score_home": 45, "score_away": 100,
            "start": datetime(2016, 9, 1, 19, 30, 0), },
           {"title": "Sconfitta di misura",
            "home_index": 1, "away_index": 9,
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

sponsors = [{"title": "Sponsor 1", "image": "loghi/viola-reggiocalabria.png"},
            {"title": "Sponsor 2", "image": "loghi/violareggiocalabria.png"},
            {"title": "Sponsor 3", "image": "loghi/violareggiocalabria.png"}]
