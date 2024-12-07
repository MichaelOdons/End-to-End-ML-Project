import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_log.log")

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Configure the logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Corrected typo: `filrHandler` -> `FileHandler`
        logging.StreamHandler(sys.stdout)  # Corrected typo: `streamHaandler` -> `StreamHandler`
    ]
)

# Get the logger
logger = logging.getLogger("mlProjectLogger")  # Corrected typo: `getlogger` -> `getLogger`
