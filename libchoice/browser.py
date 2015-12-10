import webbrowser


def get_browser(browser_name):
    return webbrowser.get('open -a "{browser}" %s'.format(browser=browser_name))


def browser_is_handler_for_url(browser, url):
    return [u for u in browser['browser']['urls'] if u in url]


def get_browser_for_url(url, settings):
    browser = next((b for b in settings['browsers'] if browser_is_handler_for_url(b, url)), None)
    if browser is None:
        return get_browser(settings['default_browser'])
    return get_browser(browser['browser']['name'])
