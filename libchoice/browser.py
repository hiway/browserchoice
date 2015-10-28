import os
import webbrowser


class Browser(object):
    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.instance = webbrowser.get('open -a "{browser}" %s'.format(browser=browser_name))

    def open(self, url):
        self.instance.open_new_tab(url)


def browser_is_handler_for_url(browser, url):
    return [u for u in browser['urls'] if u in url]


def get_browser_for_url(url, settings):
    browsers = [b for b in settings['browsers'] if browser_is_handler_for_url(b, url)]
    if not browsers:
        return Browser('Firefox')
    return Browser(browsers[0]['name'])