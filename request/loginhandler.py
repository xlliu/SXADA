# -*- coding: utf-8 -*-
import torndsession.sessionhandler
import tornado.gen
__author__ = 'xlliu'


class LoginHandler(torndsession.sessionhandler.SessionBaseHandler):

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        user = self.get_argument("user")
        pwd = self.get_argument("password")
        if user:
            if user == "fb2315":
                if pwd == "Eesh0ujoh":
                    self.session['user']=user
                    self.session['pwd']=pwd
                    self.render("monitor.html")
                else:
                    self.render("login.html",note='密码错误，请重新输入')
            else:
                self.render("login.html",note='用户名错误，请重新输入')
        else:
            self.render("login.html",note='')