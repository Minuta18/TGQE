import sys
import logging

logger = logging.getLogger('main')

try:
    import lupa.luajit21 as lupa
except ImportError:
    logger.critical('Unable to load LuaJIT 2.1. Exiting...')
    sys.exit(-1)
logger.info('LuaJIT 2.1 loaded successfully')
