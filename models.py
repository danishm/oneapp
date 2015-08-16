from google.appengine.ext import ndb

class ClickEvent(ndb.Model):

    app_key = ndb.StringProperty()
    date_time = date = ndb.DateTimeProperty(auto_now_add=True)