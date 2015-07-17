# -*- coding: utf-8 -*-
from common.requestauth import RequestAuth
import tornado.gen
__author__ = 'xlliu'


class ReAddMonitorHandler(RequestAuth):


    @tornado.gen.coroutine
    def postFunc(self):
        content = int(self.get_argument("content"))
        data = yield self.application.goMonitor.reAddMonitor(content)