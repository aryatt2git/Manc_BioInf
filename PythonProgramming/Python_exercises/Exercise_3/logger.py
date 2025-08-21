# logger.py
import logging
from logging.handlers import RotatingFileHandler
#from pathlib import Path

# Creat a logger instance
def create_logger():
    #current_directory = str(Path(__file__).resolve().parent)
    #parent_directory = str(Path(current_directory).parent)


    logger = logging.getLogger('Amino_Acid_Counter_Logger')
    logger.setLevel(logging.DEBUG)

    log_handler = RotatingFileHandler('AAC.log', maxBytes=1000000, backupCount=5)
    log_handler.setLevel(logging.DEBUG)
    log_handler_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt= '%d-%m-%Y %I:%M:%S')
    log_handler.setFormatter(log_handler_formatter)

    logger.addHandler(log_handler)

    return logger

logger = create_logger()