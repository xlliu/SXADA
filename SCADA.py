#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import AppServer
from common.config import Config
from common.config import WhileReadConfigFile
CONFIG_FILE = 'db.cfg'
APP_CONFIG_SECTION = 'dbMeg'

def run():
    onLoadConfig = Config(CONFIG_FILE,APP_CONFIG_SECTION)
    WhileReadConfigFile(onLoadConfig).start()

    httpServer = HTTPServer(AppServer(onLoadConfig),xheaders=True)
    httpServer.listen(port=8091)
    print "http://localhost:8091/monitor"
    IOLoop.instance().start()

if __name__ == '__main__':
    run()
