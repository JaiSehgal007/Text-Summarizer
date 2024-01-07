# mentioning the custom log, this could be used in any project
import os
import sys
import logging

# it will tell from which folder and time at which the logs are getting created
logging_str = "[%(asctime)s %(levelname)s: %(module)s: %(message)s]"
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath), #log created inside this file
        logging.StreamHandler(sys.stdout) # it gets displayed in the terminal as well
    ]
)

logger = logging.getLogger("textSummarizerLogger")