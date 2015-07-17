# -*- coding: utf-8 -*-
from common.authhandler import AuthHandler
import tornado.gen
__author__ = 'xlliu'


class PageMonitorHandler(AuthHandler):

    @tornado.gen.coroutine
    def postFunc(self):
        screen = int(self.get_argument('screen'))
        currentpage = int(self.get_argument('currentpage'))
        yield self.application.goMonitor.monitor