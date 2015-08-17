"""A function that posts a tracking event to Google Analytics."""

import urllib
import logging

from google.appengine.api import urlfetch

# Set this to the specific Google Analytics Tracking Id for your application.
GA_TRACKING_ID = "UA-8121060-11"
GA_CLIENT_ID = "555"


def track_event_to_ga(category, action, label=None, value=None):
    """ Posts an Event Tracking message to Google Analytics. """

    form_fields = {
        "v": "1",  # Version.
        "tid": GA_TRACKING_ID,  # Tracking ID / Web property / Property ID.
        "cid": GA_CLIENT_ID,  # Anonymous Client ID.
        "t": "event",  # Event hit type.
        "ec": category,  # Event Category. Required.
        "ea": action,  # Event Action. Required.
        "el": label,  # Event label.
        "ev": value,  # Event value.
    }
    form_data = urllib.urlencode(form_fields)
    result = urlfetch.fetch(url="http://www.google-analytics.com/collect",
                            payload=form_data,
                            method=urlfetch.POST,
                            headers={"Content-Type": "application/x-www-form-urlencoded"})

    logging.info('Recorded GA Event [fields: %s, result: %s]', form_fields, result.status_code )

    return result.status_code