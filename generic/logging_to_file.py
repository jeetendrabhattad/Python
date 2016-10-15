import logging

logging.basicConfig(filename='log_to_file.out', level=logging.ERROR)
logging.debug('This message should go to the log file')
logging.error('This message should go to the log file')
logging.critical('This message should go to the log file')
