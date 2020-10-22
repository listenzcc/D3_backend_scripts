# File: __init__.py
# Aim: Web app server in flask

import os
import configparser
from configparser import ConfigParser

# Initialization
cfg = ConfigParser()

# Loading configures
cfg.read(os.path.join(__file__, '..', 'config.ini'))

# Setup path configures
try:
    pathmode = cfg.get('server', 'apathmode')
except configparser.NoOptionError:
    pathmode = 'relative'

# For absolute path
if cfg.get('server', 'pathmode') == 'absolute':
    src_path = cfg.get('server', 'src_path')

# For relative path
if cfg.get('server', 'pathmode') == 'relative':
    src_path = cfg.get('server', 'src_path')
    src_path = os.path.join(__file__, '..', src_path)