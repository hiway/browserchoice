# browserchoice


## Installation
* Download source: `git clone https://github.com/hiway/browserchoice.git`
* Install development version: `pip install --editable .`

## Configuration
Config file: `~/.browserchoice`

    browsers:
    - browser: 
      name: Google Chrome
      urls: 
        - gmail.com
        - google.com
    - browser:
      name: Firefox
      urls: 
        - github.com 
        - twitter.com
    - browser:
      name: Safari
      urls: 
        - facebook.com
        - instagram.com

## Usage:

* Test from command line: `browserchoice http://github.com`
* Note the output of: `which browserchoice`
* Install LinCastor app
  * [Get LinCastor here](https://onflapp.wordpress.com/lincastor/)
  * ![Setup instructions for LinCastor](http://imgur.com/E5LrQsE)
* Install RCDefaultApp
  * [Get RCDefaultApp here](http://www.rubicode.com/Software/RCDefaultApp/)
  * ![Setup instructions for RCDdefaultApp](http://imgur.com/UWM7BLN)
* Test if applied system-wide: `open http://github.com`