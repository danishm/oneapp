import os
import urllib

import jinja2
import webapp2

import data


class HomeScreen(webapp2.RequestHandler):

    def get(self):
        model = {'applications':data.applications}
        template = JINJA_ENVIRONMENT.get_template('homescreen.html')
        self.response.write(template.render(model))


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


app = webapp2.WSGIApplication([
    ('/', HomeScreen),
], debug=True)