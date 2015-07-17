# -*- coding: utf-8 -*-
from common.requestauth import RequestAuth
import tornado.gen
__author__ = 'xlliu'


class ResultDetailsListHandler(RequestAuth):
    
    @tornado.gen.coroutine
    def postFunc(self):
        fbid = int(self.get_argument("fbid"))
        currentpage = int(self.get_argument("currentpage",0))
        datas = yield self.application.goMonitorDetails.goDetails(fbid=fbid,currentPage=currentpage)
        totalmonitornum = yield self.application.goMonitorDetails.countDetails(fbid=fbid)
        totalmonitorpage = (int(self.application.config.pagemonitordetailsnum)+totalmonitornum-1)/int(self.application.config.pagemonitordetailsnum)-1
        if totalmonitorpage==-1:
            totalmonitorpage=0
        self.render("resultDetailsList.html",datas = datas,currentpage=currentpage,totalmonitorpage=totalmonitorpage)