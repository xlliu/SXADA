# -*- coding: utf-8 -*-
import tornado.web
import tornado.gen
import torndsession.sessionhandler
__author__ = 'xlliu'


class RequestAuth(torndsession.sessionhandler.SessionBaseHandler):

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.postFunc()

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        if 'user' not in self.session or  'pwd'  not in self.session:
            self.render("login.html",note='')
        else:
            user = self.session['user']
            pwd = self.session['pwd']
            if user:
                if user == "fb2315":
                    if pwd == "Eesh0ujoh":
                        yield self.getFunc()
                    else:
                        self.render("login.html",note='密码错误，请重新输入')
                else:
                    self.render("login.html",note='用户名错误，请重新输入')
            else:
                self.render("login.html",note='')


    @tornado.gen.coroutine
    def postFunc(self):
        pass

    @tornado.gen.coroutine
    def getFunc(self):
        pass