# -*- coding: utf-8 -*-


import glob
import importlib
import inspect
import jemmy  # required to avoid "parent module not loaded, cannot perform relative import" error
import logging
import os


_logger = logging.getLogger(__name__)


class Plugin:
    @staticmethod
    def elevator_pitch(plugin):
        return str(plugin.__name__) + ": " + plugin.__doc__


class Plugins:
    """Collects all jemmy plugins and provides access."""
    def __init__(self):
        super(Plugins, self).__init__()
        self._plugins = []
        current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        current_module_name = os.path.splitext(os.path.basename(current_dir))[0]
        for file in glob.glob(current_dir + "/*.py"):
            file_name = os.path.splitext(os.path.basename(file))[0]

            # Ignore __ files
            if file_name.startswith("__"):
                continue

            _logger.debug("checking module ", file_name)
            module = importlib.import_module(file_name, package=current_module_name)
            for class_name, obj in inspect.getmembers(module):
                _logger.debug("found ", class_name)
                if inspect.isclass(obj) and issubclass(obj, Plugin) and class_name is not Plugin.__name__:
                    self._plugins.append(obj)

    def list(self):
        print("The following jemmy plugins are available:")
        if self._plugins:
            for plugin in self._plugins:
                print(Plugin.elevator_pitch(plugin))
        else:
            print("No jemmy plugins found.")

    def get(self, plugin):
        matches = list(filter(lambda p: p.__name__ == plugin, self._plugins))
        if len(matches) > 1:
            _logger.fatal("Found multiple plugins matching {0}".format(plugin))
            return None
        elif len(matches) < 1:
            _logger.fatal("No plugin found matching {0}".format(plugin))
            return None

        return matches[0]
