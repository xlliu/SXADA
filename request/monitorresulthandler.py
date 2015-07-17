# -*- coding: utf-8 -*-
from common.requestauth import RequestAuth
import tornado.gen
__author__ = 'xlliu'


class MonitorResultHandler(RequestAuth):


    @tornado.gen.coroutine
    def getFunc(self):
        self.render('monitorResult.html')