# -*- coding: utf-8 -*-
from common.requestauth import RequestAuth
import tornado.gen
__author__ = 'xlliu'


class LoginHandler(RequestAuth):

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        user = self.get_argument("user")
        pwd = self.get_argument("password")
        if user:
            if user == "fb2315":
                if pwd == "Eesh0ujoh":
                    self.set_secure_cookie("user",user)
                    self.redirect("/monitor")
                else:
                    self.render("login.html",note='密码错误，请重新输入')
            else:
                self.render("login.html",note='用户名错误，请重新输入')
        else:
            self.render("login.html",note='')


    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        if not self.get_secure_cookie("user"):
            self.render("login.html",note="")
            return
        self.redirect("/monitor")