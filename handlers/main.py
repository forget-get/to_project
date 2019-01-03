from tornado.web import RequestHandler

class MainHandler(RequestHandler):
    def get(self):
        self.render('main.html')


class ExploreHandler(RequestHandler):
    def get(self):
        self.render('explore.html')


class PostHandler(RequestHandler):
    def get(self,post_id):
        self.render('post.html',post_id=post_id)