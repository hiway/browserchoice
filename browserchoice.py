#!/usr/bin/env python

import click
import sys

from libchoice.config import Config
from libchoice.browser import Browser


def handle(url):
    conf = Config()
    conf.load()

    return url, 'ok'


@click.command()
@click.argument('urls', nargs=-1)
def browserchoice(urls):
    if not urls:
        print('Usage: browserchoice URL')
    result = [handle(url) for url in urls]
    print result
    sys.exit(0)


if __name__ == '__main__':
    browserchoice()
