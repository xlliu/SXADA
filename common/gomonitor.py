# -*- coding: utf-8 -*-
from common.basedb import BaseDBHandler
import tornado.gen

__author__ = 'xlliu'


class GoMonitor(BaseDBHandler):

    @tornado.gen.coroutine
    def monitorManage(self,screen,currentpage=0):
        data = None
        if screen == "all":
            data = yield self._db[self.app.config.monitorcollection].find(limit=int(self.app.config.pagemonitornum),
                                                                          skip=int(self.app.config.pagemonitornum)*currentpage).sort('last_timeline_time',-1).to_list(None)
        if screen == "ing":
            data = yield self._db[self.app.config.monitorcollection].find({'status':1},
                                                                          limit=int(self.app.config.pagemonitornum),
                                                                          skip=int(self.app.config.pagemonitornum)*currentpage).sort('last_timeline_time',-1).to_list(None)
        if screen == "log":
            data = yield self._db[self.app.config.monitorcollection].find({'status':-1},
                                                                          limit=int(self.app.config.pagemonitornum),
                                                                          skip=int(self.app.config.pagemonitornum)*currentpage).sort('last_timeline_time',-1).to_list(None)
        raise tornado.gen.Return(data)

    @tornado.gen.coroutine
    def getTotalMonitorNum(self,screen):
        data = None
        if screen == "all":
            data = yield self._db[self.app.config.monitorcollection].find().count()
        if screen == "ing":
            data = yield self._db[self.app.config.monitorcollection].find({'status':1}).count()
        if screen == "log":
            data = yield self._db[self.app.config.monitorcollection].find({'status':-1}).count()
        raise tornado.gen.Return(data)

    @tornado.gen.coroutine
    def addMonitor(self,fbId):
        data = yield self._db[self.app.config.monitorcollection].insert({
          "_id": fbId,
          "update_time" : None,
          "name" : None,
          "last_timeline_time" : None,
          "timeline_count" : None,
          "type" : None,
          "status" : 1
        })

        raise tornado.gen.Return(data)

    @tornado.gen.coroutine
    def reAddMonitor(self,fbId):
        data = yield self._db[self.app.config.monitorcollection].update({"_id":int(fbId)},{'$set':{"status":1}})

    # @tornado.gen.coroutine
    # def delMonitor(self,fbId):
    #     data = yield self._db[self.app.config.monitorcollection].remove({"_id":fbId})
    #
    #     raise tornado.gen.Return(data)

    @tornado.gen.coroutine
    def delMonitor(self,fbId):
        data = yield self._db[self.app.config.monitorcollection].update({"_id":int(fbId)},{'$set':{"status":-1}})
        # data = yield self._db[self.app.config.monitorcollection].update({"_id":int(fbId)},{"last_timeline_time" : 1433834159,"name" : "Benson Luk","status" : 1,"timeline_count" : 51,  "type" : "User","update_time" : '2015-06-11T09:59:09.892Z'})