import logging
import sys
import os

logger = logging.getLogger(__name__)
logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))  # set a default log level of INFO
_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(_handler)
