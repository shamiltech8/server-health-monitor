import logging
import os
from datetime import datetime

os.makedirs("../logs",exist_ok=True)
log_filename = f"../logs/health_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logging.basicConfig(...)
def write_log(message):write_log("CPU Usage: 20%")
