import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]: %(message)s ',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG,
                    filename='log.txt')

logger = logging.getLogger('test_logger')


logger.info('This will not show')
logger.warning('This will')
logger.debug('This is debug message')
logger.critical('This is critical error occurred ')

