# -*- coding: utf-8 -*-
from common.basedb import BaseDBHandler
import tornado.gen
__author__ = 'xlliu'


class GoMonitorDetails(BaseDBHandler):

    @tornado.gen.coroutine
    def goDetails(self,fbid,currentPage = 0):
        data = yield self._db[self.app.config.monitordetailscollection].find({'user_id':fbid},
                                                                      limit=int(self.app.config.pagemonitordetailsnum),
                                                                      skip=int(self.app.config.pagemonitordetailsnum)*currentPage).sort('last_timeline_time',-1).to_list(None)

        raise tornado.gen.Return(data)

    @tornado.gen.coroutine
    def countDetails(self,fbid):
        data = yield self._db[self.app.config.monitordetailscollection].find({"user_id":fbid}).count()

        raise tornado.gen.Return(data)