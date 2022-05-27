import logging
import datetime as td

"""
logging-Levels:
    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL
"""

# If in some cases the configuration of the logging level does not work, the following lines might fix it
for handler in logging.root.handlers:
    logging.root.removeHandler(handler)

logging.basicConfig(level=logging.DEBUG)  # Set the level of logs which will be written to the commandline

# Basic loging to the commandline
logging.log(logging.INFO, "This is our first logging message")
logging.log(logging.DEBUG, "This is our first logging message")
logging.log(logging.WARNING, "This is our first logging message")
logging.log(logging.ERROR, "This is our first logging message")
logging.log(logging.CRITICAL, "This is our first logging message")

logging.info("Test")

# logging with name definition fpr a logger
logger = logging.getLogger("myLogger")
logger.info("This is some information")

# Define the format of the logs
log_format = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")

# logging to a file and the commandline
today = td.datetime.today()  # Set the current date as filename of the logfile, so that the files dont get too big
filename = f"{today.year}-{today.month:02d}-{today.day:02d}.log"

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.WARNING)  # Set the Level of logs which will be written to the file
file_handler.setFormatter(log_format)

logger.addHandler(file_handler)

logger.debug("Hey I am debug")
logger.info("Hey I am info")
logger.warning("Hey I am warning")

