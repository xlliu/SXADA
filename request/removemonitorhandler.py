# -*- coding: utf-8 -*-
from common.requestauth import RequestAuth
import tornado.gen
__author__ = 'xlliu'


class RemoveMonitorHandler(RequestAuth):

    @tornado.gen.coroutine
    def postFunc(self):
        rem_id = self.get_argument('content')
        yield self.application.goMonitor.delMonitor(rem_id)