# -*- coding: utf-8 -*-
from parruc.devtools import profiled
from parruc.violareggiocalabria import utils
from plone import api
from Products.Five.browser import BrowserView


#  from parruc.violareggiocalabria import _


class WipView(BrowserView):

    @profiled(threshold=10)
    def get_banners(self, number=2):
        query = {"portal_type": "Banner",
                 "position": "vertical"}
        all_banners = list(api.content.find(**query))
        all_weights = [banner.weight for banner in all_banners]
        number = min(number, len(all_banners))
        banners = []
        for i in range(number):
            index = utils.weighted_choice(all_weights)
            del(all_weights[index])
            banners.append(all_banners.pop(index))
        return [banner.getObject() for banner in banners]
