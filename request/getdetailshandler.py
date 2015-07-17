# -*- coding: utf-8 -*-
from common.requestauth import RequestAuth
import tornado.gen
__author__ = 'xlliu'


class GetDetailsHandler(RequestAuth):


    @tornado.gen.coroutine
    def getFunc(self):
        fbid = self.get_argument("fbid")
        self.render("monitordetails.html",fbid=fbid)
