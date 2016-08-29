import logging

logging.basicConfig(filename='log_to_file.out', level=logging.DEBUG)
logging.debug('This message should go to the log file')
