#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import jemmy.plugins
import sys

__author__ = "Raphael Knaus"
__copyright__ = __author__
__license__ = "Don't Be a Jerk"
__version__ = "0.0.2"

_logger = logging.getLogger(__name__)


def __has_method(obj, method):
    attribute = getattr(obj, method, None)
    return callable(attribute)


def main(args):
    parser = argparse.ArgumentParser(
        description=(
            "An experimental decryption assistant supporting you in solving GeoCaching mysteries based on encryption. "
            "Use at own risk."))
    parser.add_argument('-v', '--version', action='version', version='jemmy {ver}'.format(ver=__version__))
    parser.add_argument('-p', '--plugin', action='store')
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument('-c', '--ciphertext', action='store', help='The ciphertext to decrypt or crack.')
    # input_group.add_argument(
    #     '-f',
    #     '--cipherfile',
    #     action='store',
    #     help='The file containing the ciphertext to decrypt or crack.')
    parser.add_argument('-t', '--threshold', type=int, action='store', default=65, help='threshold in percent')
    command_group = parser.add_mutually_exclusive_group(required=True)
    command_group.add_argument('-l', '--list', action='store_true', help='List all available jemmy plugins.')
    command_group.add_argument(
        '-d', '--decrypt',
        action='store_true',
        help='--decrypt --plugin PLUGIN --ciphertext CIPHERTEXT\nDecrypt CIPHERTEXT with plugin PLUGIN.')
    # TODO(KNR): later support optional --key KEY
    command_group.add_argument(
        '-a', '--analyze',
        action='store_true',
        help='--analyze --plugin PLUGIN --ciphertext CIPHERTEXT\nAnalyze CIPHERTEXT with plugin PLUGIN.')
    args = parser.parse_args(args)

    all_plugin_types = jemmy.plugins.Plugins()
    if args.list:
        all_plugin_types.list()
        return

    if not args.plugin:
        parser.print_help()
        print("Error: No plugin defined.")
        sys.exit(1)
    if not args.ciphertext:
        parser.print_help()
        print("Error: No CIPHERTEXT given.")
        sys.exit(1)

    plugin_type = all_plugin_types.get(args.plugin)
    plugin = plugin_type(dic=[])  # TODO(KNR): empty dic
    if args.decrypt:
        if not __has_method(plugin, 'decrypt'):
            parser.print_help()
            print('Error: plugin "{}" does not support operation "decrypt"'.format(type(plugin).__name__))
            sys.exit(1)
        print(plugin.decrypt(ciphertext=args.ciphertext))
        # TODO(KNR): crack command not implemented?!
    elif args.analyze:
        if not __has_method(plugin, 'analyze'):
            parser.print_help()
            print('Error: plugin "{}" does not support operation "analyze"'.format(type(plugin).__name__))
            sys.exit(1)
        result = plugin.analyze(ciphertext=args.ciphertext, threshold_percent=args.threshold)
        print('{}: {} (score: {})'.format('Match' if result.match else 'No match', result.comment, result.score))


def run():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main(args=sys.argv[1:])


if __name__ == "__main__":
    run()
