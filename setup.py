#!/bin/env python3

import os

# Create borfee home and set permissions
cmd = 'mkdir -p /opt/borfee/conf && chmod 755 -R /opt/borfee'
os.system(cmd)

# add borfee binary to $PATH
cmd = 'chmod 755 borfee/borfee.py && ln -s $(pwd)/borfee/borfee.py /usr/local/bin/borfee'
os.system(cmd)

# cp help.txt to borfee home conf
cmd = 'cp docs/help.txt /opt/borfee/conf/'
os.system(cmd)

