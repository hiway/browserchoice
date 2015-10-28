import os
import yaml

from .dictutil import dotdictify

class Config(object):
    def __init__(self, path='~/.browserchoice'):
        self.config_path = os.path.expanduser(path)
        self.settings = {}

    def load(self):
        if not os.path.exists(self.config_path):
            open(self.config_path, 'a').close()

        with open(self.config_path, 'r') as stream:
            self.settings = dotdictify(yaml.load(stream))

    def save(self):
        with open(self.config_path, 'w') as stream:
            yaml.dump(dict(self.settings), stream)

