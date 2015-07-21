# -*- coding: utf-8 -*-
import os
from tornado.ioloop import IOLoop
from common.gomonitor import GoMonitor
from common.gomonitordetails import GoMonitorDetails
from common.gomonitorresult import GoMonitorResult
from request.addmonitor import AddMonitorHandler
from request.getdetailshandler import GetDetailsHandler
from request.loadtable import LoadTable
from request.loginhandler import LoginHandler
from request.monitor import MonitorHandler
import tornado.gen
from request.monitorresulthandler import MonitorResultHandler
from request.newresultlisthandler import NewResultListHandler
from request.readdmonitor import ReAddMonitorHandler
from request.removemonitorhandler import RemoveMonitorHandler
from request.resultdetailslisthandler import ResultDetailsListHandler
from request.resultlisthandler import ResultListHandler

__author__ = 'xlliu'

import tornado.web

class AppServer(tornado.web.Application):


    def __init__(self,cfg):
        self.config = cfg

        handlers = [
            (r"/login",LoginHandler),
            (r"/monitor",MonitorHandler),
            (r"/loadtable",LoadTable),
            (r"/monitorResult",MonitorResultHandler),
            (r"/addmonitor",AddMonitorHandler),
            (r"/readdmonitor",ReAddMonitorHandler),
            (r"/removemontitor",RemoveMonitorHandler),
            (r"/resultList",ResultListHandler),
            (r"/newResultList",NewResultListHandler),
            (r"/details",GetDetailsHandler),
            (r"/resultDetailsList",ResultDetailsListHandler),
        ]

        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__),"templates"),
            static_path = os.path.join(os.path.dirname(__file__),"static"),
            cookie_secret = "61oETzKXQAGeYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url = "/login",
            debug = True
        )
        tornado.web.Application.__init__(self,handlers,**settings)

        self.goMonitor = GoMonitor(self,
                                  'monitorhost',
                                  'monitorport',
                                  'monitordbname',
                                  'monitoruser',
                                  'monitorpwd')

        self.goMonitorResult = GoMonitorResult(self,
                                  'monitorresulthost',
                                  'monitorresultport',
                                  'monitorresultdbname',
                                  'monitorresultuser',
                                  'monitorresultpwd')

        self.goMonitorDetails = GoMonitorDetails(self,
                                                  'monitordetailshost',
                                                  'monitordetailsport',
                                                  'monitordetailsdbname',
                                                  'monitordetailsuser',
                                                  'monitordetailspwd')

        IOLoop.instance().run_sync(self.init)

    @tornado.gen.coroutine
    def init(self):
        yield self.goMonitor.connectionDB()
        yield self.goMonitorResult.connectionDB()
        yield self.goMonitorDetails.connectionDB()