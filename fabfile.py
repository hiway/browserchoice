from fabric.api import *


def remove_old_link():
    with settings(quiet=True):
        local('unlink /Users/harshad/bin/browserchoice')


def compile():
    local('nuitka --recurse-all --remove-output browserchoice.py')
    local('mv browserchoice.exe browserchoice')
    remove_old_link()
    local('ln -s /Users/harshad/dev/browserchoice/browserchoice /Users/harshad/bin/browserchoice')


def link():
    remove_old_link()
    local('ln -s /Users/harshad/dev/browserchoice/browserchoice.py /Users/harshad/bin/browserchoice')
