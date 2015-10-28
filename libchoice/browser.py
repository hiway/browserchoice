import os
import webbrowser


class Browser(object):
    def __init__(self, browser_name):
        self.browser_name = browser_name
        self.instance = webbrowser.get('open -a "{browser}" %s'.format(browser=browser_name))

    def open(self, url):
        self.instance.open_new_tab(url)
