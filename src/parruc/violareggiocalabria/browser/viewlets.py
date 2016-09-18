# -*- coding: utf-8 -*-
from parruc.devtools import profiled
from parruc.violareggiocalabria import utils
from plone import api
from plone.app.layout.viewlets import common as base


class SponsorViewlet(base.ViewletBase):
    @profiled(threshold=10)
    def get_sponsors(self):
        query = {"portal_type": "Sponsor"}
        sponsors = api.content.find(**query)
        for sponsor in sponsors:
            yield sponsor.getObject()


class BannerViewlet(base.ViewletBase):
    @profiled(threshold=10)
    def get_banner(self):
        query = {"portal_type": "Banner",
                 "position": "horizzontal"}
        banners = api.content.find(**query)
        weights = [banner.weight for banner in banners]
        banner = banners[utils.weighted_choice(weights)]
        return banner.getObject()
