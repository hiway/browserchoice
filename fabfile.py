from fabric.api import *

def compile():
    local('nuitka --recurse-all --remove-output browserchoice.py')
    local('mv browserchoice.exe browserchoice')
    local('unlink /Users/harshad/bin/browserchoice')
    local('ln -s /Users/harshad/dev/browserchoice/browserchoice /Users/harshad/bin/browserchoice')

def link():
    local('unlink /Users/harshad/bin/browserchoice')
    local('ln -s /Users/harshad/dev/browserchoice/browserchoice.py /Users/harshad/bin/browserchoice')
