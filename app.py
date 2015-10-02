import os
import urllib

import jinja2
import webapp2

import data
import json
import models
import analytics

from mdetect import UAgentInfo

class HomeScreen(webapp2.RequestHandler):

    def get(self):
        user_agent = str(self.request.headers['User-Agent'])
        http_accept = str(self.request.headers['Accept'])
        ua_info = UAgentInfo(user_agent, http_accept)


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

        # Sending analytics event
        analytics.track_event_to_ga('ClickEvent', key, app['name'])

        return webapp2.redirect(app['url'])


class Debug(webapp2.RequestHandler):

    def get(self):
        user_agent = str(self.request.headers['User-Agent'])
        http_accept = str(self.request.headers['Accept'])
        ua_info = UAgentInfo(user_agent, http_accept)

        capabilities = dict()

        for obj in dir(ua_info):
            attr = getattr(ua_info, obj)
            if callable(attr) and obj.startswith('detect'):
                capabilities[obj] = attr()

        print capabilities
        self.response.headers['Content-Type'] = 'application/json' 
        self.response.write(json.dumps(capabilities))


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


app = webapp2.WSGIApplication([
    ('/', HomeScreen),
    ('/debug/', Debug),
    ('/go/(.*)/', LinkRouter)
], debug=True)