__author__ = 'zengyuetian'

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("You requested the main page")


class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You request the story " + story_id)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/([0-9]+)", StoryHandler),
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
