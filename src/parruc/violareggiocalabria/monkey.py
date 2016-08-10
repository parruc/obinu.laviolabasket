# -*- coding: utf-8 -*-
from DateTime import DateTime
from plone.app.content import utils
from z3c.relationfield import RelationValue

import datetime
import Missing


def custom_json_handler(obj):
    if obj == Missing.Value:
        return None
    if type(obj) in (datetime.datetime, datetime.date):
        return obj.isoformat()
    if type(obj) in (DateTime, ):
        dt = DateTime(obj)
        return dt.ISO()
    if type(obj) in (RelationValue, ):
        return ""
    return obj

utils.custom_json_handler = custom_json_handler
