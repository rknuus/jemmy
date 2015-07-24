#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
import logging
import plugins


__author__ = "Raphael Knaus"
__copyright__ = "Raphael Knaus"
__license__ = "none"
__version__ = "0.0.1"

_logger = logging.getLogger(__name__)


def parse_args(args):
    parser = argparse.ArgumentParser(
        description="An experimental decryption assistant supporting you in solving GeoCaching mysteries based on encryption. Use at own risk.")
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='jemmy {ver}'.format(ver=__version__))
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-l',
        '--list',
        action='store_true')
    return parser.parse_args(args)


def main(args):
    args = parse_args(args)
    if args.list:
        all_plugins = plugins.Plugins()
        all_plugins.list()


def run():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
