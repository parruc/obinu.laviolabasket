# -*- coding: utf-8 -*-
from parruc.violareggiocalabria import utils
from plone import api
from plone.batching import Batch
from Products.Five.browser import BrowserView


#  from parruc.violareggiocalabria import _


class BaseNews(BrowserView):
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

    def format_news_date(self, date):
        return utils.format_date(date, month_length=3)


class NewsItemView(BaseNews):
    pass


class NewsView(BaseNews):

    def batched_news(self):
        query = {"portal_type": "News Item",
                 "sort_on": "effective",
                 "sort_order": "descending",}
        news = api.content.find(**query)
        pagenumber = int(self.request.get("p", "1"))
        batch = Batch.fromPagenumber(items=news, pagesize=6,
                                     pagenumber=pagenumber, navlistsize=0)
        return batch

    def create_paging_link(self, pagenumber):
        return self.context.absolute_url() + "?p=%d" % pagenumber

    def format_news_date(self, date):
        return utils.format_date(date, month_length=3)
