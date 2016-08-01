# -*- coding: utf-8 -*-
from datetime import datetime
from parruc.violareggiocalabria import _


base_perm = "parruc.violareggiocalabria: Add "


folders = [{"title": _(u"Partite"), "permission": base_perm + "Partita",
            "exclude_from_nav": False},
           {"title": _(u"Roster"), "permission": base_perm + "Giocatore",
            "exclude_from_nav": False},
           {"title": _(u"News"), "permission": base_perm + "News Item",
            "exclude_from_nav": False},
           {"title": _(u"Sponsor"), "permission": base_perm + "Sponsor",
            "exclude_from_nav": True},
           {"title": _(u"Partner"), "permission": base_perm + "Partner",
            "exclude_from_nav": True},
           {"title": _(u"Squadre"), "permission": base_perm + "Squadra",
            "exclude_from_nav": True},
           {"title": _(u"Società"),
            "exclude_from_nav": False},
           {"title": _(u"Video"), "permission": base_perm + "Video",
            "exclude_from_nav": True},
           {"title": _(u"Slide"), "permission": "parruc.flexslider: Add Slide",
            "exclude_from_nav": True},
           {"title": _(u"Giovanili"),
            "exclude_from_nav": False}, ]

pages = [{"title": _(u"Storia"), 'parent': "societa"},
         {"title": _(u"Club"), 'parent': "societa"},
         {"title": _(u"Pala Calafiore"), 'parent': "societa"},
         {"title": _(u"Caffè Mauro"), },
         {"title": _(u"Contatti")}, ]

teams = [{"title": u"Givova Scafati", "played": 30, "points": 40,
          "image_logo": "loghi/givova-scafati.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"BCC Agropoli", "played": 30, "points": 38,
          "image_logo": "loghi/bcc-agropoli.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"Orsi Tortona", "played": 30, "points": 38,
          "image_logo": "loghi/orsi-tortona.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"FMC Ferentino", "played": 30, "points": 36,
          "image_logo": "loghi/mfc-ferentino.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"Mens Sana Basket 1871 Siena", "played": 30, "points": 36,
          "image_logo": "loghi/menssana-siena.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"Moncada Agrigento", "played": 30, "points": 34,
          "image_logo": "loghi/moncada-agrigento.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"Lighthouse Conad Trapani", "played": 30, "points": 32,
          "image_logo": "loghi/lighthouseconad-trapani.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"Novipiù Casale Monferrato", "played": 30, "points": 30,
          "image_logo": "loghi/novapiu-casale.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"Bermé Reggio Calabria", "played": 30, "points": 28,
          "image_logo": "loghi/viola-reggiocalabria.png",
          "image_teaser": "teaser2.jpg"},
         {"title": u"Angelico Biella", "played": 30, "points": 28,
          "image_logo": "loghi/angelico-biella.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"Assigeco Casalpusterlengo", "played": 30, "points": 26,
          "image_logo": "loghi/assigeco-casalpusterlengo.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"Benacquista Ass. Latina", "played": 30, "points": 26,
          "image_logo": "loghi/nologo.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"Npc Rieti", "played": 30, "points": 26,
          "image_logo": "loghi/npc-rieti.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"Acea Roma", "played": 30, "points": 26,
          "image_logo": "loghi/acea-roma.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"Paffoni Omegna", "played": 30, "points": 24,
          "image_logo": "loghi/paffoni-omegna.png",
          "image_teaser": "teaser1.jpg"},
         {"title": u"La Briosa Barcellona", "played": 30, "points": 12,
          "image_logo": "loghi/briosa-barcellona.png",
          "image_teaser": "teaser1.jpg"}, ]


partite = [{"title": u"Vittoria al cardiopalma",
            "home_index": 8, "away_index": 5,
            "score_home": 100, "score_away": 99,
            "start": datetime(2016, 7, 1, 15, 30, 0), },
           {"title": u"Vittoria al cardiopalma",
            "home_index": 8, "away_index": 9,
            "score_home": 100, "score_away": 99,
            "start": datetime(2016, 8, 1, 15, 30, 0), },
           {"title": u"Grande vittoria fuori casa",
            "home_index": 2, "away_index": 8,
            "score_home": 45, "score_away": 100,
            "start": datetime(2016, 9, 1, 19, 30, 0), },
           {"title": u"Sconfitta di misura",
            "home_index": 1, "away_index": 8,
            "score_home": 98, "score_away": 110,
            "start": datetime(2016, 10, 1, 21, 30, 0), }, ]

slides = [{"title": u"La viola mette a segno punti preziosi",
           "url": "/",
           "image": "slide1.jpg"},
          {"title": u"Un'altra vittoria per i ragazzi della Viola",
           "url": "/",
           "image": "slide2.jpg"}, ]

videos = [{"title": u"Coach Frates post Viola Tortona",
           "url": "https://www.youtube.com/embed/BFTz_-bIVuM"},
          {"title": u"Valerio Costa post Viola Casalpusterlengo",
          "url": "https://www.youtube.com/embed/18Op_UYJEYw"},
          {"title": u"Coach Bolignano post Viola Trapani",
           "url": "https://www.youtube.com/embed/YjnDyeSrgYo"},
          {"title": u"Roberto Rullo post Viola Trapani",
           "url": "https://www.youtube.com/embed/rzlLYloWQpM"}
          ]
players = [{"name": "Ion", "surname": "Lupusor", "role": "Ala"},
           {"name": "Lorenzo", "surname": "Caroti", "role": "Playmaker"},
           {"name": "Tommaso", "surname": "Guariglia", "role": "Cenntro"},
           {"name": "Celis", "surname": "Taflaj", "role": "Guardia"}, ]

news = [{"title": u"News diprova 1",
         "description": "Questa è una news di prova"},
        {"title": u"News diprova 2",
         "description": "Questa è una news di prova"},
        {"title": u"News diprova 3",
         "description": "Questa è una news di prova"},
        {"title": u"News diprova 4",
         "description": "Questa è una news di prova"},
        {"title": u"News diprova 5", "description":
         "Questa è una news di prova"}, ]

partners = [{"title": u"Partner 1", "image": "loghi/viola-reggiocalabria.png"},
            {"title": u"Partner 2", "image": "loghi/viola-reggiocalabria.png"},
            {"title": u"Partner 3", "image": "loghi/viola-reggiocalabria.png"}]

sponsors = [{"title": u"Sponsor 1", "image": "loghi/viola-reggiocalabria.png"},
            {"title": u"Sponsor 2", "image": "loghi/viola-reggiocalabria.png"},
            {"title": u"Sponsor 3", "image": "loghi/viola-reggiocalabria.png"}]
