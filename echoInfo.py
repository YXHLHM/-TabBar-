from config.config import Config
import os
c = Config()
print(f'ENV:{c.env()}')

config = c.cfg
print(f'CONFIG:')
for i in config:
    print(f'\t{i}:{config[i]}')
environ = os.environ
print(f'ENVIRON:')
for i in environ:
    print(f'\t{i}:{environ[i]}')