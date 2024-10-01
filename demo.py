from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys


# Ensure the logger is initialized
logging.info("aWAHHHHHH")

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e, sys)