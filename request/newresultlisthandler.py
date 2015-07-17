# -*- coding: utf-8 -*-
from common.requestauth import RequestAuth
import tornado.gen
__author__ = 'Administrator'


class NewResultListHandler(RequestAuth):


    @tornado.gen.coroutine
    def postFunc(self):
        datas = yield self.application.goMonitorResult.newMonitorResult()
        self.render("resultList.html",datas=datas,totalmonitorpage=0,currentpage=0)