import os
import time

def cleanup_logs():

    log_directory = "../logs"

    for file in os.listdir(log_directory):

        file_path = os.path.join(log_directory, file)

        if os.path.isfile(file_path):

            file_age = time.time() - os.path.getmtime(file_path)

            if file_age > 7 * 24 * 60 * 60:

                os.remove(file_path)

                print(f"Deleted old log: {file}")
