from parruc.violareggiocalabria import utils
from plone import api
from plone.app.layout.viewlets import common as base


class ControlPanelViewlet(base.ViewletBase):

    def get_links(self):
        for item in ["partite", "squadre", "news", "giocatori", "video", ]:
            yield{"title": item, "url": getattr(utils, item+"_link")(add=True)}


class SponsorViewlet(base.ViewletBase):

    def get_sponsors(self):
        query = {"portal_type": "Sponsor"}
        sponsors = api.content.find(**query)
        for sponsor in sponsors:
            yield sponsor.getObject()


class BannerViewlet(base.ViewletBase):

    def get_banners(self):
        query = {"portal_type": "Banner"}
        banners = api.content.find(**query)
        for banner in banners:
            yield banner.getObject()

    def get_banner(self):
        query = {"portal_type": "Banner", "sort_limit": 1}
        banners = api.content.find(**query)
        return banners[0].getObject()
