# -*- coding: utf-8 -*-
import tornado.web
import tornado.gen
__author__ = 'xlliu'


class AuthHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.postFunc()

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.getFunc()

    @tornado.gen.coroutine
    def postFunc(self):
        pass

    @tornado.gen.coroutine
    def getFunc(self):
        pass