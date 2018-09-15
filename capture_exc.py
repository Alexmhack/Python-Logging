import logging

a = 'logger'
b = 0

try:
	b = int(a)
except Exception as e:
	logging.error("Exception Occured", exc_info=True)
