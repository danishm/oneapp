import os
import urllib

import jinja2
import webapp2

import data
import models


class HomeScreen(webapp2.RequestHandler):

    def get(self):
        model = {'applications':data.applications}
        template = JINJA_ENVIRONMENT.get_template('homescreen.html')
        self.response.write(template.render(model))


class LinkRouter(webapp2.RequestHandler):

    def get(self, key):
        app = data.get_application_map()[key]

        # Storing click event
        click_event = models.ClickEvent()
        click_event.app_key = app['key']
        click_event.put()
        print 'Click Event Saved'

        return webapp2.redirect(app['url'])

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


app = webapp2.WSGIApplication([
    ('/', HomeScreen),
    ('/go/(.*)/', LinkRouter)
], debug=True)