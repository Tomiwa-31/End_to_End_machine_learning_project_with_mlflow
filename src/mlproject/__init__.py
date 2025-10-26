import os
import sys
import logging

#sets up our custom logger

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),  ## ✅ Saves to file
        logging.StreamHandler(sys.stdout)   # shows in terminal
    ]
)

logger = logging.getLogger("mlProjectLogger")