# coding=utf-8
# author = ZengYueTian
# date = 2015-04-01

__author__ = 'zengyuetian'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.escape

import uuid
import os.path
# import concurrent.futures
# import markdown
import bcrypt
import subprocess
import requests
import re
import subprocess
import unicodedata
import redis

from tornado.options import define, options
from tornado import gen
from SimpleDB import *
from settings import *


define("port", default=80, help="run on the given port", type=int)

testcases = []
devices = []
db = None

# A thread pool to be used for password hashing with bcrypt.
# executor = concurrent.futures.ThreadPoolExecutor(2)


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("user")
        if not user_id:
            return None
        return db.GET_USER_BY_ID(user_id)[0]["name"]

    def any_user_exists(self):
        return db.GET_USER_COUNT() > 0



########################################
# register a user
########################################
class AuthCreateHandler(BaseHandler):
    def get(self):
        self.render("auth_create.html", error=None)

    @gen.coroutine
    def post(self):

        username = self.get_argument("username")
        user = db.GET_USER_BY_NAME(username)
        if user:
            self.render("auth_create.html", error="user already exist")

        hashed_password = tornado.escape.utf8(self.get_argument("password"))
        # hashed_password = yield exector.submit(
        #     bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
        #     bcrypt.gensalt())

        author_id = db.INSERT_USER(username, hashed_password)

        self.set_secure_cookie("user", str(author_id))
        self.render("index.html")
        # self.redirect(self.get_argument("next", "/"))




########################################
# login as user
########################################
class AuthLoginHandler(BaseHandler):
    def get(self):
        # if there are no users, redirect to the account creation page
        if not self.any_user_exists():
            self.redirect("/auth/create")
        else:
            self.render("auth_login.html", error=None)

    @gen.coroutine
    def post(self):
        user = db.GET_USER_BY_NAME(self.get_argument("username"))

        if not user:
            self.render("auth_login.html", error="user not found")
            return

        hash_password = tornado.escape.utf8(self.get_argument("password"))
        # hash_password = yield executor.submit(
        #     bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
        #     tornado.escape.utf8(user.hashed_password)

        if hash_password == user[0]["hashed_password"]:
            self.set_secure_cookie("user", str(user[0]["id"]))
            self.redirect("/test/view")
        else:
            self.render("auth_login.html", error="incorrect password")



class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.render("index.html")


#index page
class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.render("index.html")


#about page
class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.render('dashboard.html', user=name)



#add test case to server
class TestAddHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.render('test_add.html', user=name)

class TestUploadHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        name = tornado.escape.xhtml_escape(self.current_user)

        fileinfo = self.request.files['filearg'][0]
        print "fileinfo is", fileinfo
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open("uploads/"+ cname, 'w')
        fh.write(fileinfo['body'])
        case_id = self.get_argument("caseid")
        id = db.GET_USER_BY_NAME(name)[0]["id"]
        # self.finish(cname + " is uploaded!! Check %s folder" %__UPLOADS__)
        db.INSERT_TESTCASE(case_id, cname, id)
        self.render('test_upload.html', file=cname, user=name)

class TestSubmitHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.render('task_submit.html', user=name, testcase="", device="")

    @tornado.web.authenticated
    def post(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        testcase = self.get_argument("testcase")
        device = self.get_argument("device")
        array = device.split("+")
        os = array[0].strip()
        mode = array[1].strip()
        # print os, mode
        device_id = db.GET_DEVICE_ID(os, mode)[0]["id"]
        # print device_id
        testcase_id = db.GET_TESTCASE_ID_BY_USER_AND_CASE(name, testcase)[0]["id"]
        # print "testcase_id ->", testcase_id
        db.INSERT_TASK(testcase_id, device_id, "submit")

        self.render('task_submit.html', user=name, testcase=testcase, device=device)

# about page
class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('about.html')

# view task in list
class TaskViewHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        global testcases
        tasks = db.GET_TASK_BY_USER(name)
        # print tasks
        self.render('task_view.html', user=name, tasks=tasks)


# view task in list
class TaskUpdateHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        task_id = self.get_argument("task_id")
        status = self.get_argument("status")
        db.UPDATE_TASK(task_id, status)


# view test in test list
class TestViewHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        global testcases
        testcases = db.GET_TESTCASE_BY_USER(name)
        self.render('test_view.html', tcs=testcases, user=name)

    @tornado.web.authenticated
    def post(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        global testcases
        testcases = db.GET_TESTCASE_BY_USER(name)
        self.render('test_view.html', tcs=testcases, user=name)

# view test in test list
class TestRunHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        global testcases, devices
        testcases = db.GET_TESTCASE_BY_USER(name)
        devices = db.GET_DEVICE()
        self.render('test_run.html', tcs=testcases, user=name, devices=devices)




########################################
# server Application
########################################
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/main", MainHandler),
            (r"/auth/create", AuthCreateHandler),
            (r"/auth/login", AuthLoginHandler),
            (r"/auth/logout", AuthLogoutHandler),
            (r"/test/add", TestAddHandler),
            (r"/test/upload", TestUploadHandler),
            (r"/test/view", TestViewHandler),
            (r"/test/run", TestRunHandler),
            (r"/test/submit", TestSubmitHandler),
            (r"/task/view", TaskViewHandler),
            (r"/task/update", TaskUpdateHandler),
            (r"/about", AboutHandler),

        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            data_path=os.path.join(os.path.dirname(__file__), "data"),
            xsrf_cookies=False,
            cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url="/auth/login",


            debug=True,
        )

        global db
        db = SimpleDB()

        tornado.web.Application.__init__(self, handlers, **settings)

        # have one global connection to the DB across all handlers




# main workflow start from here
if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



