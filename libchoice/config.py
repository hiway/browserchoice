import os
import yaml


class Config(object):
    def __init__(self, path='~/.browserchoice'):
        self.config_path = os.path.expanduser(path)
        self.settings = {'browsers':[{
                'default_browser':'Firefox',
                'browser': [
                {'name': 'Google Chrome'},
                {'urls': ['gmail.com', 'google.com']}
            ]}], }

    def load(self):
        if not os.path.exists(self.config_path):
            self.save()

        with open(self.config_path, 'r') as stream:
            self.settings = yaml.load(stream)

    def save(self):
        with open(self.config_path, 'w') as stream:
            yaml.dump(self.settings, stream)
