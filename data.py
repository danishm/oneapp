applications = [
    {
        'key': 'facebook',
        'name': 'Facebook',
        'url': 'https://m.facebook.com/'
    },
    {
        'key': 'twitter',
        'name': 'Twitter',
        'url': 'https://mobile.twitter.com/'
    },
    {
        'key': 'linkedin',
        'name': 'LinkedIn',
        'url': 'https://touch.www.linkedin.com/?rs=false&redirectUrl=%23stream&ahoy=no#stream'
    },
    {
        'key': 'google-maps',
        'name': 'Google Maps',
        'url': 'https://www.google.com/maps/'
    },
    {
        'key': 'gmail',
        'name': 'Gmail',
        'url': 'https://mail.google.com/'
    },
    {
        'key': 'google',
        'name': 'Google',
        'url': 'https://www.google.com/'
    },
    {
        'key': 'weather-channel',
        'name': 'Weather Channel',
        'url': 'http://m.weather.com/'
    },
    {
        'key': 'mta',
        'name': 'NYC Subway',
        'url': 'http://m.mta.info/'
    },
    {
        'key': 'google-news',
        'name': 'News',
        'url': 'https://news.google.com/'
    },
    {
        'key': 'reddit',
        'name': 'Reddit',
        'url': 'https://m.reddit.com/'
    },
    {
        'key': 'nytimes',
        'name': 'New York Times',
        'url': 'http://mobile.nytimes.com/'
    }

]

APP_MAP = None


def get_application_map():
    global APP_MAP

    if APP_MAP is None:
        APP_MAP = {}
        for app in applications:
            APP_MAP[app['key']] = app

    return APP_MAP