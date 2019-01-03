import tornado.web
import tornado.ioloop
import tornado.options
from tornado.options import define,options

from handlers import main

define('port', default='8080' ,help='run port', type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/',main.MainHandler),
            ('/explore',main.ExploreHandler),
            ('/post/(?P<post_id>[0-9]+)',main.PostHandler),
        ]
        settings = dict(
            template_path = 'templates',
            static_path = 'static',
            static_url_prefix='/tutu/',
            debug = True,
        )
        super().__init__(handlers, **settings)

application =  Application()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
    