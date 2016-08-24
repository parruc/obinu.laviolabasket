from parruc.violareggiocalabria import _
from plone.app.vocabularies.catalog import CatalogSource
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


viola_teams = CatalogSource(path={'query': "/", 'depth': -1},
                            portal_type=("Squadra", ), is_viola="True")

teams = CatalogSource(path={'query': "/", 'depth': -1},
                      portal_type=("Squadra", ))

launches = CatalogSource(path={'query': "/", 'depth': -1},
                         portal_type=("Document", "News Item"))

leagues = CatalogSource(path={'query': "/", 'depth': -1},
                        portal_type=("League", ))


# def _get_terms_from_registry(voc_name):
#     registry = queryUtility(IRegistry)
#     terms = []
#     if not registry:
#         return terms
#     items = registry.get(voc_name, {})
#     for key, value in items.items():
#         terms.append(SimpleTerm(key, key, _(value)))
#     return terms


match_types = SimpleVocabulary(
    [SimpleTerm(value=u'regular', title=_(u'Campionato regolare')),
     SimpleTerm(value=u'playoff', title=_(u'Playoff')),
     SimpleTerm(value=u'playout', title=_(u'Playout')),
     SimpleTerm(value=u'friendly', title=_(u'Amichevole')),
     ])

banner_positions = SimpleVocabulary(
    [SimpleTerm(value=u'horizzontal', title=_(u'Orizzontale')),
     SimpleTerm(value=u'vertical', title=_(u'Verticale')),
     ])

video_categories = SimpleVocabulary(
    [SimpleTerm(value=u'regular', title=_(u'Campionato')),
     SimpleTerm(value=u'tournament', title=_(u'Tornei')),
     SimpleTerm(value=u'interview', title=_(u'Interviste')),
     ])
