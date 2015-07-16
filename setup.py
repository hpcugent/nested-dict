#!/usr/bin/env python
#
# Copyright (C) 2015 Leo Goodstadt <nested_dict@llew.org.uk>
#
# This file is part of nested_dict.
#
# nested_dict is free software: you can redistribute it and/or modify
# it under the terms of the MIT license as found here
# http://opensource.org/licenses/MIT.
#

# Adapted for use at HPC UGent by Andy Georges

import os
import re
import sys

import vsc.install.shared_setup as shared_setup

shared_setup.SHARED_TARGET.update({
    'url': 'https://github.com/bunbun/nested-dict',
    'download_url': ('',),
})


# originally, had 2.7, but seems to work with 2.6.6 as well
if not sys.version_info[0:2] >= (2, 6, 6):
    sys.stderr.write("Requires Python later than 2.6.6\n")
    sys.exit(1)


# Following the recommendations of PEP 396 we parse the version number
# out of the module.
def parse_version(module_file):
    """
    Parses the version string from the specified file.
    This implementation is ugly, but there doesn't seem to be a good way
    to do this in general at the moment.
    """
    f = open(module_file)
    s = f.read()
    f.close()
    match = re.findall("__version__ = '([^']+)'", s)
    return match[0]


f = open(os.path.join(os.path.dirname(__file__), "README.rst"))
nested_dict_readme = f.read()
f.close()
nested_dict_version = parse_version(os.path.join("lib/nested_dict", "__init__.py"))

PACKAGE = {
    "name": "nested-dict",
    "version": nested_dict_version,
    "description": "Python dictionary with automatic and arbitrary levels of nestedness",
    "long_description": nested_dict_readme,
    "packages": ["nested_dict"],
    "author": ['Leo Goodstadt'],
    "author_email": 'nested_dict@llew.org.uk',
    "url": "http://pypi.python.org/pypi/nested_dict",
    "keywords": ["nested", "dict", "defaultdict", "dictionary", "auto-vivification"],
    "license": "MIT",

    "classifiers": [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Developers",
        'Intended Audience :: Information Technology',
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ],
}

# python setup.py register
# flake8 *.py tests --exclude=ez_setup.py --max-line-length=100
# nosetests --with-coverage --cover-package nested_dict --cover-inclusive --cover-min-percentage 85
# make -C docs html
# git tag -a v1.5.1 -m "Version 1.5.1"
# python setup.py sdist --format=gztar,zip upload

if __name__ == '__main__':
    shared_setup.action_target(PACKAGE)
