# -*- coding: utf-8 -*-
from common.requestauth import RequestAuth
import tornado.gen
__author__ = 'xlliu'


class LoadTable(RequestAuth):


    @tornado.gen.coroutine
    def postFunc(self):
        screen = self.get_argument('screen','all')
        currentpage = int(self.get_argument('currentpage',0))
        accountList = yield self.application.goMonitor.monitorManage(screen=screen,currentpage=currentpage)
        totalmonitorpage = yield self.application.goMonitor.getTotalMonitorNum(screen=screen)
        totalmonitorpage = (totalmonitorpage+int(self.application.config.pagemonitornum)-1)/int(self.application.config.pagemonitornum)-1
        if totalmonitorpage==-1:
            totalmonitorpage=0
        self.render("loadtable.html",accountList=accountList,totalmonitorpage=totalmonitorpage,currentpage=currentpage)