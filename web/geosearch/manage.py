#!/usr/bin/env python

# Python
import datetime
import os
from pprint import pprint
import readline
import sys
# Packages
from flask import *
# Project
from datapunt_geosearch import create_app


def shell():
    """Start app shell"""
    os.environ['PYTHONINSPECT'] = 'True'


def run_server():
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8000)


def run_server_prod():
    # Starts the server with prod settings
    from datapunt_geosearch import config
    app = create_app(config)
    app.run(host='0.0.0.0', port=8000)


def help_txt():
    print ("run - start dev server\nshell - start an interactive shell\ncreate - create the geoindex in elastic\nrecreate - drop the old index and create a new one in elastic")


def main():
    # Parsing args
    if len(sys.argv) == 1:
        shell()
    else:
        if sys.argv[1] == 'run':
            run_server()
        elif sys.argv[1] =='run_prod':
            run_server_prod()
        elif sys.argv[1] == 'shell':
            shell()
        elif sys.argv[1] == 'help':
            help_txt()
        else:
            print('Unkown command, options:')
            help_txt()


if __name__ == '__main__':
    main()