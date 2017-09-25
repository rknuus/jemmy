#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import jemmy.plugins
import sys

__author__ = "Raphael Knaus"
__copyright__ = "Raphael Knaus"
__license__ = "none"
__version__ = "0.0.1"

_logger = logging.getLogger(__name__)


def main(args):
    parser = argparse.ArgumentParser(
        description=
        "An experimental decryption assistant supporting you in solving GeoCaching mysteries based on encryption. Use at own risk.")
    parser.add_argument('-v', '--version', action='version', version='jemmy {ver}'.format(ver=__version__))
    parser.add_argument('-p', '--plugin', action='store')
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument('-t', '--ciphertext', action='store', help='The ciphertext to decrypt or crack.')
    # input_group.add_argument(
    #     '-f',
    #     '--cipherfile',
    #     action='store',
    #     help='The file containing the ciphertext to decrypt or crack.')
    command_group = parser.add_mutually_exclusive_group(required=True)
    command_group.add_argument('-l', '--list', action='store_true', help='List all available jemmy plugins.')
    command_group.add_argument(
        '-d', '--decrypt',
        action='store_true',
        help=
        '--decrypt --plugin PLUGIN [--key KEY] --ciphertext CIPHERTEXT\nDecrypt CIPHERTEXT with plugin PLUGIN and using the optional key KEY.')
    args = parser.parse_args(args)

    all_plugin_types = jemmy.plugins.Plugins()
    if args.list:
        all_plugin_types.list()
    elif args.decrypt:
        if not args.plugin:
            parser.print_help()
            print("Error: No plugin defined.")
            sys.exit(1)
        if not args.ciphertext:
            parser.print_help()
            print("Error: No CIPHERTEXT given.")
            sys.exit(1)
        plugin_type = all_plugin_types.get(args.plugin)
        plugin = plugin_type(dic=[])
        print(plugin.decrypt(ciphertext=args.ciphertext))


def run():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main(args=sys.argv[1:])


if __name__ == "__main__":
    run()
