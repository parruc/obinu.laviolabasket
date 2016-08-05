from parruc.violareggiocalabria import _
from plone.app.vocabularies.catalog import CatalogSource
from plone.registry.interfaces import IRegistry
from zope.component import queryUtility
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


viola_teams = CatalogSource(path={'query': "/", 'depth': -1},
                            portal_type=("Squadra", ), Subject="viola")

teams = CatalogSource(path={'query': "/", 'depth': -1},
                      portal_type=("Squadra", ))

launches = CatalogSource(path={'query': "/", 'depth': -1},
                         portal_type=("Document", "News Item"))


def _get_terms_from_registry(voc_name):
    registry = queryUtility(IRegistry)
    terms = []
    if not registry:
        return terms
    items = registry.get(voc_name, {})
    for key, value in items.items():
        terms.append(SimpleTerm(key, key, _(value)))
    return terms


class LeaguesVocabulary(object):
    """
    """
    implements(IVocabularyFactory)

    def __call__(self, context, query=None):
        terms = _get_terms_from_registry(
            'parruc.violareggiocalabria.vocabularies.leagues'
        )
        return SimpleVocabulary(terms)


LeaguesVocabularyFactory = LeaguesVocabulary()
