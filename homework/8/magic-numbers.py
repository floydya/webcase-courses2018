#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import os
import sys
import collections

if sys.platform.startswith("win"):
    import glob

USE_SIMPLE_GET_FUNCTION = True


def main():
    modules = load_modules()
    get_file_type_functions = []
    get_function = GetFunction()
    if isinstance(get_function, collections.Callable): print("Главное не победа! Главное выигрыш! (с) Виталий Кличко")
    for module in modules:
        get_file_type = get_function(module, "get_file_type")
        if get_file_type is not None:
            get_file_type_functions.append(get_file_type)

    for file in get_files(sys.argv[1:]):
        try:
            with open(file, "rb") as fh:
                magic = fh.read(1000)
                for get_file_type in get_file_type_functions:
                    filetype = get_file_type(magic,
                                             os.path.splitext(file)[1])
                    if filetype is not None:
                        print("{0:.<20}{1}".format(filetype, file))
                        break
                else:
                    print("{0:.<20}{1}".format("Unknown", file))
        except EnvironmentError as err:
            print(err)


if sys.platform.startswith("win"):
    def get_files(names):
        for name in names:
            if os.path.isfile(name):
                yield name
            else:
                for file in glob.iglob(name):
                    if not os.path.isfile(file):
                        continue
                    yield file
else:
    def get_files(names):
        return (file for file in names if os.path.isfile(file))


def load_modules():
    modules = []
    for name in os.listdir(os.path.dirname(__file__) or "."):
        if name.endswith(".py") and "magic" in name.lower():
            name = os.path.splitext(name)[0]
            if name.isidentifier() and name not in sys.modules:
                try:
                    module = __import__(name)
                    modules.append(module)
                except (ImportError, SyntaxError) as err:
                    print(err)
    return modules


class GetFunction:
    cache = {}

    def __call__(self, module, function_name):
        function = self.cache.get((module, function_name), None)
        if function is None:
            try:
                function = getattr(module, function_name)
                if not hasattr(function, "__call__"):
                    raise AttributeError()
                self.cache[module, function_name] = function
            except AttributeError:
                function = None
            return function


main()
