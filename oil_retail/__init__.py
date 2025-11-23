import os
import sys
import logging

logging_str = "[ %(asctime)s ] %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
log_dir = "log"
log_filepath = os.path.join(log_dir, "running_logs.log")

os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("oil_retail")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(logging_str)

if not logger.handlers:
    # File handler
    file_handler = logging.FileHandler(log_filepath)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Stream handler
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)