from os import (system as s,
                path as pth,
                getcwd as gcwd)

import logging
logging.basicConfig(level = logging.DEBUG,
              filename = r'logs.log',
              format = '%(asctime)s : %(levelname)s : %(message)s',
              filemode = 'a')

s('mode con cols=25 lines=4')
s('taskkill /f /im Miner.exe')
logging.debug('Miner.exe exit')
c_path = gcwd()
s(pth.join(c_path, 'Miner.exe'))
logging.debug('Miner.exe started')
