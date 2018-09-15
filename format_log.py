import logging

logging.basicConfig(filename='py.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning("Warning will get logged to file")
