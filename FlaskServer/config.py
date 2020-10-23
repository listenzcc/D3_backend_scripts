# File: config.py
# Aim: Maintaince the config and logging of the package

# Imports
import configparser
import logging
import logging.config
import os
import pandas as pd

# %%


class Config(object):
    def __init__(self, logger):
        self.config = pd.DataFrame()
        self.logger = logger

    def append(self, group, name, value):
        self.config = self.config.append(pd.Series(dict(GROUP=group,
                                                        NAME=name,
                                                        VALUE=value)),
                                         ignore_index=True)
        self.logger.debug(
            f'Append new config: "{group}":"{name}" as "{value}"')

    def display(self):
        # Display the config
        print(self.config)

    def query(self, group, name, ignore_not_found=True):
        result = self.config.query(f'GROUP=="{group}" & NAME=="{name}"')
        num = len(result)

        if num == 0:
            self.logger.error(
                f'No records found for {group}: {name}')
            if ignore_not_found:
                # Ignore the notFound error
                return None
            else:
                raise Exception(f'No records found for {group}: {name}')

        if num > 1:
            self.logger.warning(
                f'Multiple ({num}) records found for {group}: {name}')

        return result.iloc[-1].VALUE


# %%
# Initialize the parser
parser = configparser.ConfigParser()

# Loading configures
parser.read(os.path.join(__file__, '..', 'config.ini'))

# Setup logger
mode = parser.get('Logging', 'mode')
filepath = parser.get('Logging', 'filepath')
configpath = os.path.join(__file__, '..', 'logging.ini')
logging.config.fileConfig(configpath, defaults={'filepath': filepath})
logger = logging.getLogger(mode)
logger.info(f'Logger initialized at "{mode}" mode')

# Setup config
config = Config(logger)

# %%
# --------------------------------------------------------
# Setup directory configures
try:
    mode = parser.get('SrcDirectory', 'mode')
except configparser.NoOptionError:
    mode = 'relative'

src = parser.get('SrcDirectory', 'directory')

# For relative path
if mode == 'relative':
    src = os.path.join(__file__, '..', src)

config.append('Directory', 'src', src)

# Setup MIME types
for option in parser.options('MIMEType'):
    config.append('KnownType', option, parser.get('MIMEType', option))

# Setup charset
for option in parser.options('Charset'):
    config.append('Charset', option, parser.get('Charset', option))

# Report what we got
config.logger.debug('Configure is loaded: \n{}'.format(config.config))
