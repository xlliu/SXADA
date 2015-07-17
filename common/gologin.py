# -*- coding: utf-8 -*-
from bson import objectid
import time
from common.basedb import BaseDBHandler
import tornado.gen
__author__ = 'xlliu'


class GoLogin(BaseDBHandler):

    @tornado.gen.coroutine
    def get_user_by_pwd(self, owner, password):
        data = yield self._db[self.app.config.owner_collection].find_one({'owner':owner, 'password':password}, {'cookie':1})
        raise tornado.gen.Return(data)

    @tornado.gen.coroutine
    def check_user(self, ownerid, cookie):
        if ownerid and cookie:
            try:
                owner = yield self._db[self.app.config.owner_collection].find_one({'_id':objectid.ObjectId(ownerid), 'cookie':cookie}, {'owner':1, 'update_time':1})
            except:
                pass
            else:
                if owner:
                    raise tornado.gen.Return(owner)