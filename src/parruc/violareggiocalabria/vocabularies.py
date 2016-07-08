from plone.app.vocabularies.catalog import CatalogSource

teams = CatalogSource(path={'query': "/violareggiocalabria/", 'depth': -1},
                      portal_type=("Squadra", ))

launches = CatalogSource(path={'query': "/violareggiocalabria/", 'depth': -1},
                      portal_type=("Document", "News Item"))
