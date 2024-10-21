import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    format='[%(levelname)s] %(asctime)s %(module)s.%(funcName)s: %(message)s', 
    filename='app.log', 
    level=logging.DEBUG
)

if __name__ == '__main__':
    pass
