# -*- coding: utf-8 -*-
from common.basedb import BaseDBHandler
import tornado.gen
__author__ = 'xlliu'


class GoMonitorResult(BaseDBHandler):

    @tornado.gen.coroutine
    def monitorResult(self,currentPage=0):
        data = yield self._db[self.app.config.monitorresultcollection].find({'time':{'$ne':""}},limit = int(self.app.config.pagemonitorresultnum),
                                                                            skip =int(self.app.config.pagemonitorresultnum)*currentPage ).sort('time',-1).to_list(None)
        raise tornado.gen.Return(data)

    @tornado.gen.coroutine
    def newMonitorResult(self):
        data = yield self._db[self.app.config.monitorresultcollection].find({'time':{'$ne':""}},limit =20).sort('time',-1).to_list(None)
        raise tornado.gen.Return(data)

    @tornado.gen.coroutine
    def countMonitorResult(self):
        data = yield self._db[self.app.config.monitorresultcollection].find({'time':{'$ne':""}}).count()

        raise tornado.gen.Return(data)