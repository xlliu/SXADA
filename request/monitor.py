# -*- coding: utf-8 -*-
import tornado.gen
from common.requestauth import RequestAuth

__author__ = 'xlliu'


class MonitorHandler(RequestAuth):

    @tornado.gen.coroutine
    def getFunc(self):
        self.render("monitor.html")

    @tornado.gen.coroutine
    def postFunc(self):
        pass