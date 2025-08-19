# logger.py
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Creat a logger instance
def create_logger():
    current_directory = str(Path(__name__).resolve().parent)
    parent_directory = str(Path(current_directory).parent)

    logger = logging.getLogger('Amino_Acid_Counter_Logger')
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(stream_handler_formatter)

    log_handler = RotatingFileHandler(f'{current_directory}/git_repos/Manc_BioInf/PythonProgramming/logs/AAC.log', maxBytes=1000000, backupCount=5)
    log_handler.setLevel(logging.ERROR)
    log_handler_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(log_handler_formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(log_handler)

    return logger

log = create_logger()