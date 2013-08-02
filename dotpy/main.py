#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""dotpy

.dotfiles distribution management

Usage:
    dotpy build (<slice>... | --all)
    dotpy symlink (<slice>... | --all)
    dotpy copy (<slice>... | --all)
    dotpy merge (<slice>... | --all)
    dotpy cd (slice)
    dotpy list
    dotpy (-h | --help)
    dotpy --version


Options:
    --config=<file>     set configfile to use
    -h --help           show this help message and exit
    --version           show program's version number and exit

"""

import sys

from docopt import docopt
from . import __version__ as version


def main():
    "Run the main programm."
    args = docopt(__doc__, version='dotpy version '+ version)

    ## find out what configfile to use


    if args['build']:
        print 'build'

    elif args['symlink']:
        print 'symlink'

    elif args['copy']:
        print 'copy'

    elif args['merge']:
        print 'merge'

    elif args['cd']:
        print 'cd'




    print args

    sys.exit(0)
