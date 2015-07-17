# -*- coding: utf-8 -*-
from common.requestauth import RequestAuth
import tornado.gen
__author__ = 'Administrator'


class ResultListHandler(RequestAuth):


    @tornado.gen.coroutine
    def postFunc(self):
        currentPage = int(self.get_argument("currentpage",0))
        datas = yield self.application.goMonitorResult.monitorResult(currentPage=currentPage)
        totalmonitornum = yield self.application.goMonitorResult.countMonitorResult()
        totalmonitorpage = (int(self.application.config.pagemonitorresultnum)+totalmonitornum-1)/int(self.application.config.pagemonitorresultnum)-1
        if totalmonitorpage==-1:
            totalmonitorpage=0
        self.render("resultList.html",datas=datas,totalmonitorpage=totalmonitorpage,currentpage=currentPage)