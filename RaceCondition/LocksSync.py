import threading
import logging
import time
from concurrent.futures import ThreadPoolExecutor

class DB:
    # basic settings of the database
    def __init__(self):
        # value as 0
        self.value = 0
        # threading lock - mutual exclusion lock for the threads
        self.lock = threading.Lock()

    def LockUpdate(self, name):
        logging.info(f"Thread {name}: starting update")
        logging.debug(f"Thread {name} about to lock")
        with self.lock:
            logging.debug(f"Thread {name} has lock")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.5)
            self.value = local_copy
            logging.debug(f"Thread {name} about to release lock")
        logging.debug(f"Thread {name} after release")
        logging.info(f"Thread {name} finishing update")


if __name__ == "__main__":
    format = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=format, datefmt="%H:%M:%S")

    # database initialization
    database = DB()

    logging.info("Testing update using locks this time...")
    logging.info(f"Starting value is {database.value}")
    with ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.LockUpdate, index)
    logging.info(f"Finished value is {database.value}")
