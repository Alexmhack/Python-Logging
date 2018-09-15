import logging

# create a custom logger
logger = logging.getLogger(__name__)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')

c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)
