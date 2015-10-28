#!/usr/bin/env python

import click
import sys

from libchoice.config import Config
from libchoice.browser import Browser, get_browser_for_url


def handle(url):
    conf = Config()
    conf.load()
    browser = get_browser_for_url(url, conf.settings)
    browser.open(url)


@click.command()
@click.argument('urls', nargs=-1)
def browserchoice(urls):
    if not urls:
        print('Usage: browserchoice URL')
    [handle(url) for url in urls]
    sys.exit(0)

