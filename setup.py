#!/bin/env python3

import os

# Create borfee home and set permissions

# add borfee binary to $PATH
cmd = 'chmod 755 borfee/borfee.py && ln -s $(pwd)/borfee/borfee.py /usr/local/bin/borfee'
os.system(cmd)
