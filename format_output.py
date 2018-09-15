import logging

logging.basicConfig(
	format='%(asctime)s - %(levelname)s - %(message)s - %(pathname)s',
	datefmt='%d-%b-%y %H:%M:%S'
)
logging.warning("Admin logged in")
